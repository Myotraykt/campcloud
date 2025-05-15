import { Page, expect } from '@playwright/test';

export class IanaPage {
  private readonly page: Page;

  constructor(page: Page) {
    this.page = page;
  }

  async verifyUrl() {
    await expect(this.page).toHaveURL('https://www.iana.org/help/example-domains');
  }
}
