import json

def transform_data(element):
    """
    Transforms raw cryptocurrency data into a cleaned and structured format suitable for BigQuery.

    Args:
        element (str): A JSON string representing a cryptocurrency record.

    Returns:
        str: A JSON string of the cleaned and transformed record, or None if an error occurs.

    Raises:
        Exception: If an error occurs during JSON parsing or data transformation.
    """

    try:
        record = json.loads(element.replace("'", "\""))

        # Cleaned record matching BigQuery schema
        cleaned_record = {
            "id": str(record['id']),
            "name": str(record["name"].upper()),
            "symbol": str(record["symbol"]),
            "current_price": float(record["current_price"]),
            "price_unit": "$",  # Adding a static value
            "market_cap": str(round(record["market_cap"] / 1000000000)) + " Billions",
            "ath": str(record["ath"]),
            "atl": str(record["atl"]),
            "price_change_24h": round(float(record["price_change_24h"]), 1),
            "price_change_percentage_24h": round(float(record["price_change_percentage_24h"]), 1),
            "total_volume": str(record.get("total_volume")),
            "high_24h": str(record.get("high_24h")),
            "low_24h": str(record.get("low_24h")),
            "total_supply": str(record.get("total_supply")),
            "last_updated": str(record.get("last_updated")),
        }

        print(f"Transformed Record: {cleaned_record}")
        return json.dumps(cleaned_record)

    except Exception as e:
        print(f"Error processing record: {e}, Input: {element}")
        return None