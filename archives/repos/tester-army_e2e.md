<a href="https://tester.army/e2e?utm_source=e2e&utm_medium=github&utm_campaign=readme_banner"><img src="./.github/assets/readme-banner.png" alt="e2e, the open source AI testing framework by TesterArmy" width="100%" /></a>

<p align="center">
  <a href="https://tester.army?utm_source=e2e&utm_medium=github&utm_campaign=readme_badge"><img alt="Made by TesterArmy" src="./.github/assets/made-by-testerarmy.svg" /></a>
  <a href="https://www.npmjs.com/package/e2e"><img alt="npm version" src="https://img.shields.io/npm/v/e2e.svg?style=for-the-badge&labelColor=000000" /></a>
  <a href="./LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/badge/license-Apache--2.0-green.svg?style=for-the-badge&labelColor=000000" /></a>
  <a href="https://tester.army/discord"><img alt="Join the community on Discord" src="https://img.shields.io/badge/Join%20the%20community-5865F2.svg?style=for-the-badge&logo=discord&logoColor=white&labelColor=000000" /></a>
</p>

<p align="center">
  <a href="https://www.star-history.com/tester-army/e2e"><picture><source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/badge?repo=tester-army/e2e&type=trending&theme=dark" /><img alt="GitHub Trending Repository of the Day" src="https://api.star-history.com/badge?repo=tester-army/e2e&type=trending" /></picture></a>
</p>

# e2e

[e2e](https://tester.army/e2e?utm_source=e2e&utm_medium=github&utm_campaign=readme_intro) is an end-to-end testing framework for web and mobile apps. Describe a goal in natural language and an agent drives the app to reach it. Check the result with locators and assertions in the same test.

```ts
// tests/checkout.e2e.ts
import { test, expect } from 'e2e';

test('a member upgrades to Pro', async ({ app, agent, screen }) => {
  await app.open('/settings/billing');

  await agent.act('upgrade the workspace to the Pro plan');
  await agent.assert('the invoice preview shows a prorated amount');

  await expect(screen.getByRole('status')).toContainText('

... (truncated)