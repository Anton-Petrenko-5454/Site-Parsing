import asyncio
from playwright.async_api import async_playwright

async def main():
    async with (async_playwright() as pw):
        browser = await pw.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://www.soccer.ru/matches-list/')
        all_matches = await page.query_selector_all('.view-content-matches .match')

        for match in all_matches:
            m = await match.query_selector('.not-online')
            if m is not None and await m.inner_text() == 'матч завершен':
                home_name = await (await match.query_selector('.home-row .team-name a')).inner_text()
                home_score = await (await match.query_selector('.home-row .score')).inner_text()

                visit_name = await (await match.query_selector('.visit-row .team-name a')).inner_text()
                visit_score = await (await match.query_selector('.visit-row .score')).inner_text()
                print(f'{home_name} - {visit_name}\t({home_score}:{visit_score})')
        await browser.close()


if __name__ == '__main__':
    asyncio.run(main())
