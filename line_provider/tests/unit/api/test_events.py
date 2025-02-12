from typing import Any

import pytest
from httpx import AsyncClient, Response

from line_provider.tests.fixtures import test_cases


class TestEventsHandler:

    @staticmethod
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        ('url', 'expected_status_code', 'expectation'),
        test_cases.PARAMS_TEST_GET_EVENTS,
    )
    async def test_events_get(
            url: str,
            expected_status_code: int,
            expectation: Any,
            test_async_client: AsyncClient,
    ) -> None:
        response: Response = await test_async_client.get(url)
        assert response.status_code == expected_status_code

    @staticmethod
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        ('url', 'payload', 'expected_status_code', 'expectation'),
        test_cases.PARAMS_TEST_POST_EVENTS,
    )
    async def test_events_post(
            url: str,
            payload: dict,
            expected_status_code: int,
            expectation: Any,
            test_async_client: AsyncClient,
    ) -> None:
        response: Response = await test_async_client.post(url=url, json=payload)
        assert response.status_code == expected_status_code

    @staticmethod
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        ('url', 'expected_status_code', 'expectation'),
        test_cases.PARAMS_TEST_GET_ONE,
    )
    async def test_events_get_one(
            url: str,
            expected_status_code: int,
            expectation: Any,
            test_async_client: AsyncClient,
    ) -> None:
        response: Response = await test_async_client.get(url=url)
        assert response.status_code == expected_status_code

    @staticmethod
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        ('url', 'payload', 'expected_status_code', 'expectation'),
        test_cases.PARAMS_TEST_PATCH_ONE,
    )
    async def test_events_get_one(
            url: str,
            payload: dict,
            expected_status_code: int,
            expectation: Any,
            test_async_client: AsyncClient,
    ) -> None:
        response: Response = await test_async_client.patch(url=url, json=payload)
        assert response.status_code == expected_status_code
