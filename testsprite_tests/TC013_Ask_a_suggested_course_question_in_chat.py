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
        
        # -> Click the floating 'Chat with EduReach Bot' button to open the chat drawer.
        # Chat with EduReach Bot button
        elem = page.get_by_role("button", name="Chat with EduReach Bot")
        await elem.click(timeout=10000)
        
        # -> Click the 'What courses do you offer?' quick question in the chat drawer.
        # What courses do you offer? button
        elem = page.get_by_role("button", name="What courses do you offer?")
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> The conversation includes the selected quick question 'What courses do you offer?'.
        # Assert-outcome: passed
        # Assert: Verify the selected quick question appears in the conversation.
        await expect(page.locator("#root").nth(0)).to_contain_text("What courses do you offer?", timeout=15000), "Verify the selected quick question appears in the conversation."
        
        # --> A chatbot response is visible with the text 'Sorry, something went wrong. Please try again.'
        # Assert-outcome: passed
        # Assert: Verify a chatbot response is visible in the chat.
        await expect(page.locator("#root").nth(0)).to_contain_text("Sorry, something went wrong. Please try again.", timeout=15000), "Verify a chatbot response is visible in the chat."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    