import asyncio
import re
from playwright import async_api
from playwright.async_api import expect

async def run_test():
    pw = None
    browser = None
    context = None

    try:
        # Start a Playwright session in asynchronous mode
        pw = await async_api.async_playwright().start()

        # Launch a Chromium browser in headless mode with custom arguments
        browser = await pw.chromium.launch(
            headless=True,
            args=[
                "--window-size=1280,720",
                "--disable-dev-shm-usage",
                "--ipc=host",
                "--single-process"
            ],
        )

        # Create a new browser context (like an incognito window)
        context = await browser.new_context()
        # Wider default timeout to match the agent's DOM-stability budget;
        # auto-waiting Playwright APIs (expect, locator.wait_for) inherit this.
        context.set_default_timeout(15000)

        # Open a new page in the browser context
        page = await context.new_page()

        # Interact with the page elements to simulate user flow
        # -> navigate
        await page.goto("http://localhost:4173")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Click the 'Courses' link in the navbar to open or scroll to the Courses section.
        # Courses link
        elem = page.get_by_role("link", name="Courses")
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> The Courses section is open and course program entries are visible on the page.
        # Assert-outcome: passed
        # Assert: The page URL contains the courses section fragment.
        await expect(page).to_have_url(re.compile("\\#courses"), timeout=15000), "The page URL contains the courses section fragment."
        await page.locator("#courses").get_by_text("₹7.2 LPA").nth(0).scroll_into_view_if_needed()
        # Assert-outcome: passed
        # Assert: A course card element (LPA span) in the Courses section is visible, proving program entries are listed.
        await expect(page.locator("#courses").get_by_text("₹7.2 LPA").nth(0)).to_be_visible(timeout=15000), "A course card element (LPA span) in the Courses section is visible, proving program entries are listed."
        
        # --> Seat counts and average package (LPA) information for programs are visible (example: MBA card shows seats and LPA).
        await page.locator("span").filter(has_text=re.compile(r"^60 seats$")).nth(0).scroll_into_view_if_needed()
        # Assert-outcome: passed
        # Assert: The MBA program seat-count element is visible.
        await expect(page.locator("span").filter(has_text=re.compile(r"^60 seats$")).nth(0)).to_be_visible(timeout=15000), "The MBA program seat-count element is visible."
        await page.locator("#courses").get_by_text("₹8.0 LPA").nth(0).scroll_into_view_if_needed()
        # Assert-outcome: passed
        # Assert: The MBA program average package (LPA) element is visible.
        await expect(page.locator("#courses").get_by_text("₹8.0 LPA").nth(0)).to_be_visible(timeout=15000), "The MBA program average package (LPA) element is visible."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    