import { test } from '@playwright/test';
import { ExamplePage } from '../pages/example.page';
import { IanaPage } from '../pages/iana.page';

test('Example Domain Test', async ({ page }) => {
  const examplePage = new ExamplePage(page);
  const ianaPage = new IanaPage(page);

  await examplePage.navigate();
  await examplePage.verifyTitle();
  await examplePage.clickMoreInformation();
  
  await ianaPage.verifyUrl();
});
