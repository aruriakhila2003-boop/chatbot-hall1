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
        
        # -> Click the 'Chat with EduReach Bot' button to open the chat drawer and reveal the chat input and welcome text.
        # Chat with EduReach Bot button
        elem = page.get_by_role("button", name="Chat with EduReach Bot")
        await elem.click(timeout=10000)
        
        # -> Type a custom fees question into the 'Ask a question...' input (placeholder text) and press Enter to submit.
        # Ask a question... text field
        elem = page.get_by_role("textbox", name="Ask a question...")
        await elem.wait_for(state="visible", timeout=10000)
        await elem.fill("What is the fee structure for the B.Tech Computer Science program?")
        
        # --> Assertions to verify final state
        
        # --> The submitted question appears in the chat conversation.
        # Assert-outcome: passed
        # Assert: The user's submitted question is present in the page text.
        await expect(page.locator("#root").nth(0)).to_contain_text("What is the fee structure for the B.Tech Computer Science program?", timeout=15000), "The user's submitted question is present in the page text."
        
        # --> A chatbot reply is visible in the conversation (the bot returned an error message).
        # Assert-outcome: passed
        # Assert: A chatbot reply message is visible in the conversation.
        await expect(page.locator("#root").nth(0)).to_contain_text("Sorry, something went wrong. Please try again.", timeout=15000), "A chatbot reply message is visible in the conversation."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    