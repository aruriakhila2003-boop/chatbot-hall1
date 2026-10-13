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
        
        # -> Click the 'Explore Programs of the college' call-to-action in the hero.
        # Explore Programs of the college link
        elem = page.get_by_role("link", name="Explore Programs of the")
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> The site header shows the 'EduReach' brand and the hero CTA 'Explore Programs of the college' is visible.
        # Assert-outcome: passed
        # Assert: Branding displays 'EduReach' in the navbar.
        await expect(page.locator("xpath=/html/body/div[1]/nav/div/a").nth(0)).to_have_text("EduReach", timeout=15000), "Branding displays 'EduReach' in the navbar."
        # Assert-outcome: passed
        # Assert: Hero CTA 'Explore Programs of the college' is visible.
        await expect(page.locator("xpath=/html/body/div[1]/div[1]/section[1]/div[2]/div/a").nth(0)).to_have_text("Explore Programs of the college", timeout=15000), "Hero CTA 'Explore Programs of the college' is visible."
        
        # --> Clicking the hero CTA navigated to the Courses section (URL contains '#courses').
        # Assert-outcome: passed
        # Assert: URL contains '#courses', indicating navigation to the Courses section.
        await expect(page).to_have_url(re.compile("\\#courses"), timeout=15000), "URL contains '#courses', indicating navigation to the Courses section."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    