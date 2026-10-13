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
        
        # -> Click the floating chat button titled 'Chat with EduReach Bot' to open the chat drawer.
        # Chat with EduReach Bot button
        elem = page.get_by_role("button", name="Chat with EduReach Bot")
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Chat welcome content is visible in the opened chat drawer.
        await page.locator("div > .w-8").nth(0).scroll_into_view_if_needed()
        # Assert-outcome: passed
        # Assert: The chat welcome content container is visible.
        await expect(page.locator("div > .w-8").nth(0)).to_be_visible(timeout=15000), "The chat welcome content container is visible."
        
        # --> Suggested question buttons are visible in the chat drawer.
        await page.get_by_role("button", name="What courses do you offer?").nth(0).scroll_into_view_if_needed()
        # Assert-outcome: passed
        # Assert: The 'What courses do you offer?' suggested question button is visible.
        await expect(page.get_by_role("button", name="What courses do you offer?").nth(0)).to_be_visible(timeout=15000), "The 'What courses do you offer?' suggested question button is visible."
        await page.get_by_role("button", name="Tell me about placements").nth(0).scroll_into_view_if_needed()
        # Assert-outcome: passed
        # Assert: The 'Tell me about placements' suggested question button is visible.
        await expect(page.get_by_role("button", name="Tell me about placements").nth(0)).to_be_visible(timeout=15000), "The 'Tell me about placements' suggested question button is visible."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    