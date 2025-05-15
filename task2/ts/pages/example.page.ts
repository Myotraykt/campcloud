import { Page, expect } from '@playwright/test';

export class ExamplePage {
  private readonly page: Page;

  constructor(page: Page) {
    this.page = page;
  }

  async navigate() {
    await this.page.goto('https://example.com');
  }

  async verifyTitle() {
    await expect(this.page).toHaveTitle(/Example/);
  }

  async clickMoreInformation() {
    await this.page.click('css=a:has-text("More information")');
  }
}
