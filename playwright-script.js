import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://localhost:5173/');
  await page.getByText('Est. 2005 · Hyderabad, TelanganaWelcome to EduReach CollegeYour Gateway to').click();
  await page.getByText('₹42 LPA').click();
  await page.getByText('₹42 LPA').click();
  await page.getByText('Highest Package').click();
  await page.getByText('Your Gateway to Smarter').click();
  await page.getByRole('link', { name: 'EduReach' }).click();
  await page.getByText('EduReachHomeAboutCoursesMentorsCampusPlacementsLoginSign Up').click();
  await page.getByRole('link', { name: 'Home' }).click();
  await page.getByRole('button', { name: 'Sign Up' }).click();
  await page.getByRole('button', { name: 'Sign Up' }).click();
  await page.getByRole('button', { name: 'Login' }).click();
  await page.locator('div').filter({ hasText: 'Campus Placement Drive' }).nth(5).click();
  await page.goto('http://localhost:5173/');
});