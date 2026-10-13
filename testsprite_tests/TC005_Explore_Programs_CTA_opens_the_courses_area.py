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
        
        # -> Click the "Explore Programs of the college" primary call-to-action in the hero section.
        # Explore Programs of the college link
        elem = page.get_by_role("link", name="Explore Programs of the")
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Clicking the hero CTA navigates to the courses fragment and displays the Programs Offered section with program cards visible.
        # Assert-outcome: passed
        # Assert: The URL contains the '#courses' fragment after clicking the hero CTA.
        await expect(page).to_have_url(re.compile("\\#courses"), timeout=15000), "The URL contains the '#courses' fragment after clicking the hero CTA."
        await page.locator("span").filter(has_text=re.compile(r"^60 seats$")).nth(0).scroll_into_view_if_needed()
        # Assert-outcome: passed
        # Assert: A program card seat-count element (showing '60 seats') in the courses section is visible.
        await expect(page.locator("span").filter(has_text=re.compile(r"^60 seats$")).nth(0)).to_be_visible(timeout=15000), "A program card seat-count element (showing '60 seats') in the courses section is visible."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    