# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
import requests
import json

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionShowBrands(Action):
    """Action to fetch and display brands from API with JWT token"""

    def name(self) -> Text:
        return "action_show_brands"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            # Get token from latest message metadata
            latest_message = tracker.latest_message
            token = latest_message.get("metadata", {}).get("token")
            
            if not token:
                # Fallback to mock data if no token
                dispatcher.utter_message(
                    text="Đây là các thương hiệu có sẵn:",
                    buttons=[
                        {"title": "ROLEX", "payload": "tôi muốn xem sản phẩm thương hiệu ROLEX"},
                        {"title": "DIOR", "payload": "tôi muốn xem sản phẩm thương hiệu DIOR"}
                    ]
                )
                return []

            # Call brands API with token
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }
            
            response = requests.get("http://localhost:8080/v1/brands", 
                                 headers=headers, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            brands = data.get("brands", {}).get("items", [])
            
            if not brands:
                dispatcher.utter_message(text="Hiện tại chưa có thương hiệu nào.")
                return []

            # Create buttons for each brand
            buttons = []
            for brand in brands:
                brand_name = brand.get("name", "")
                brand_id = brand.get("id", "")
                buttons.append({
                    "title": brand_name,
                    "payload": f"tôi muốn xem đồng hồ thương hiệu {brand_name}",
                    "id": brand_id,
                    "metadata": {
                        "brand_id": brand_id,
                        "intent": "filter_products"
                    }
                })

            # Send message with buttons
            dispatcher.utter_message(
                text="Đây là các thương hiệu có sẵn:",
                buttons=buttons
            )

        except requests.exceptions.RequestException as e:
            # Fallback to mock data on API error
            dispatcher.utter_message(
                text="Đây là các thương hiệu có sẵn:",
                buttons=[
                    {"title": "ROLEX", "payload": "tôi muốn xem sản phẩm thương hiệu ROLEX"},
                    {"title": "DIOR", "payload": "tôi muốn xem sản phẩm thương hiệu DIOR"}
                ]
            )
        except Exception as e:
            dispatcher.utter_message(
                text="Có lỗi xảy ra khi tải thông tin thương hiệu."
            )

        return []


class ActionShowCategories(Action):
    """Action to fetch and display categories from API with JWT token"""

    def name(self) -> Text:
        return "action_show_categories"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            # Get token from latest message metadata
            latest_message = tracker.latest_message
            token = latest_message.get("metadata", {}).get("token")
            
            if not token:
                # Fallback to mock data if no token
                dispatcher.utter_message(
                    text="Đây là các phân loại sản phẩm có sẵn:",
                    buttons=[
                        {"title": "Khải", "payload": "tôi muốn xem sản phẩm phân loại Khải"},
                        {"title": "Olympia12", "payload": "tôi muốn xem sản phẩm phân loại Olympia12"},
                        {"title": "Đồng hồ nam", "payload": "tôi muốn xem sản phẩm phân loại Đồng hồ nam"},
                        {"title": "Đồng hồ nữ", "payload": "tôi muốn xem sản phẩm phân loại Đồng hồ nữ"}
                    ]
                )
                return []

            # Call categories API with token
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }
            
            response = requests.get("http://localhost:8080/v1/categorys", 
                                 headers=headers, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            categories = data.get("categorys", {}).get("items", [])
            
            if not categories:
                dispatcher.utter_message(text="Hiện tại chưa có phân loại sản phẩm nào.")
                return []

            # Create buttons for each category
            buttons = []
            for category in categories:
                category_name = category.get("name", "")
                category_id = category.get("id", "")
                buttons.append({
                    "title": category_name,
                    "payload": f"tôi muốn xem đồng hồ danh mục {category_name}",
                    "id": category_id,
                    "metadata": {
                        "category_id": category_id,
                        "intent": "filter_products"
                    }
                })

            # Send message with buttons
            dispatcher.utter_message(
                text="Đây là các phân loại sản phẩm có sẵn:",
                buttons=buttons
            )

        except requests.exceptions.RequestException as e:
            # Fallback to mock data on API error
            dispatcher.utter_message(
                text="Đây là các phân loại sản phẩm có sẵn:",
                buttons=[
                    {"title": "Khải", "payload": "tôi muốn xem sản phẩm phân loại Khải"},
                    {"title": "Olympia12", "payload": "tôi muốn xem sản phẩm phân loại Olympia12"},
                    {"title": "Đồng hồ nam", "payload": "tôi muốn xem sản phẩm phân loại Đồng hồ nam"},
                    {"title": "Đồng hồ nữ", "payload": "tôi muốn xem sản phẩm phân loại Đồng hồ nữ"}
                ]
            )
        except Exception as e:
            dispatcher.utter_message(
                text="Có lỗi xảy ra khi tải thông tin phân loại sản phẩm."
            )

        return []


class ActionShowColors(Action):
    """Action to fetch and display colors from API with JWT token"""

    def name(self) -> Text:
        return "action_show_colors"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            # Get token from latest message metadata
            latest_message = tracker.latest_message
            token = latest_message.get("metadata", {}).get("token")
            
            if not token:
                # Fallback to mock data if no token
                dispatcher.utter_message(
                    text="Đây là các màu sắc có sẵn:",
                    buttons=[
                        {"title": "Màu đen", "payload": "tôi muốn xem sản phẩm màu đen"},
                        {"title": "Màu trắng", "payload": "tôi muốn xem sản phẩm màu trắng"},
                        {"title": "Màu vàng", "payload": "tôi muốn xem sản phẩm màu vàng"},
                        {"title": "Màu bạc", "payload": "tôi muốn xem sản phẩm màu bạc"},
                        {"title": "Màu xanh", "payload": "tôi muốn xem sản phẩm màu xanh"}
                    ]
                )
                return []

            # Call colors API with token
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }
            
            response = requests.get("http://localhost:8080/v1/colors", 
                                 headers=headers, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            colors = data.get("colors", {}).get("items", [])
            
            if not colors:
                dispatcher.utter_message(text="Hiện tại chưa có màu sắc nào.")
                return []

            # Create buttons for each color
            buttons = []
            for color in colors:
                color_name = color.get("name", "")
                color_id = color.get("id", "")
                buttons.append({
                    "title": color_name,
                    "payload": f"tôi muốn xem đồng hồ màu {color_name.lower()}",
                    "id": color_id,
                    "metadata": {
                        "color_id": color_id,
                        "intent": "filter_products"
                    }
                })

            # Send message with buttons
            dispatcher.utter_message(
                text="Đây là các màu sắc có sẵn:",
                buttons=buttons
            )

        except requests.exceptions.RequestException as e:
            # Fallback to mock data on API error
            dispatcher.utter_message(
                text="Đây là các màu sắc có sẵn:",
                buttons=[
                    {"title": "Màu đen", "payload": "tôi muốn xem sản phẩm màu đen"},
                    {"title": "Màu trắng", "payload": "tôi muốn xem sản phẩm màu trắng"},
                    {"title": "Màu vàng", "payload": "tôi muốn xem sản phẩm màu vàng"},
                    {"title": "Màu bạc", "payload": "tôi muốn xem sản phẩm màu bạc"},
                    {"title": "Màu xanh", "payload": "tôi muốn xem sản phẩm màu xanh"}
                ]
            )
        except Exception as e:
            dispatcher.utter_message(
                text="Có lỗi xảy ra khi tải thông tin màu sắc."
            )

        return []


class ActionShowPopularWatches(Action):
    """Action to fetch and display popular watches from recommendations API"""

    def name(self) -> Text:
        return "action_show_popular_watches"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            # Get token from latest message metadata
            latest_message = tracker.latest_message
            token = latest_message.get("metadata", {}).get("token")

            headers = {"Content-Type": "application/json"}
            if token:
                headers["Authorization"] = f"Bearer {token}"

            # Choose API endpoint based on token availability
            if token:
                # Use authenticated recommendations API
                response = requests.get("http://localhost:8080/v1/recommendations?limit=5", 
                                     headers=headers, timeout=10)
            else:
                # Use public recommendations API
                response = requests.get("http://localhost:8080/v1/recommendations/public?limit=5", 
                                     headers=headers, timeout=10)
            
            response.raise_for_status()
            
            data = response.json()
            # API provides recommendations in data.recommendations
            recommendations = data.get("data", {}).get("recommendations", [])
            
            if not recommendations:
                dispatcher.utter_message(text="Hiện tại chưa có mẫu đồng hồ nổi bật nào.")
                return []

            # Build cards payload for FE
            cards: List[Dict[str, Any]] = []
            for rec in recommendations:
                cards.append({
                    "id": rec.get("watch_id"),
                    "code": f"REC-{rec.get('watch_id')}",
                    "name": rec.get("name"),
                    "description": rec.get("description"),
                    "model": rec.get("name"),  # Use name as model for recommendations
                    "caseMaterial": ", ".join(rec.get("material_tags", [])),
                    "caseSize": None,  # Not available in recommendations
                    "strapSize": None,  # Not available in recommendations
                    "gender": rec.get("gender_target"),
                    "waterResistance": None,  # Not available in recommendations
                    "releaseDate": None,  # Not available in recommendations
                    "sold": rec.get("sold"),
                    "basePrice": rec.get("base_price"),
                    "rating": rec.get("rating"),
                    "status": True,  # Assume active for recommendations
                    "thumbnail": rec.get("images", [None])[0] if rec.get("images") else None,
                    "slider": rec.get("images", []),
                    "brandId": rec.get("brand", {}).get("id"),
                    "brandName": rec.get("brand", {}).get("name"),
                    "categoryId": rec.get("category", {}).get("id"),
                    "categoryName": rec.get("category", {}).get("name"),
                    "movementTypeId": None,  # Not directly available
                    "movementTypeName": ", ".join(rec.get("movement_type_tags", [])),
                    "colorTags": rec.get("color_tags", []),
                    "styleTags": rec.get("style_tags", []),
                    "priceTier": rec.get("price_tier"),
                    "sizeCategory": rec.get("size_category"),
                    "isAiRecommended": rec.get("is_ai_recommended"),
                    "score": rec.get("score")
                })

            dispatcher.utter_message(
                text="Top mẫu đồng hồ nổi bật/hot hiện tại:",
                custom={
                    "type": "cards",
                    "cards": cards
                }
            )

        except requests.exceptions.RequestException as e:
            # Fallback to mock cards on API error
            dispatcher.utter_message(
                text="Top mẫu đồng hồ nổi bật/hot hiện tại:",
                custom={
                    "type": "cards",
                    "cards": [
                        {
                            "id": "sample-1",
                            "code": "DH-01",
                            "name": "Đồng hồ mẫu 01",
                            "description": "Mẫu hot, bán chạy",
                            "model": "01",
                            "caseMaterial": "titan",
                            "caseSize": 40,
                            "strapSize": 20,
                            "gender": "0",
                            "waterResistance": "IP68",
                            "releaseDate": "2025-10-01",
                            "sold": 10,
                            "basePrice": 2499000,
                            "rating": 5,
                            "status": True,
                            "thumbnail": "https://via.placeholder.com/300x300",
                            "slider": []
                        }
                    ]
                }
            )
        except Exception as e:
            dispatcher.utter_message(
                text="Có lỗi xảy ra khi tải thông tin đồng hồ bán chạy."
            )

        return []


class ActionShowMovementTypes(Action):
    """Action to fetch and display movement types from API with JWT token"""

    def name(self) -> Text:
        return "action_show_movement_types"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            # Get token from latest message metadata
            latest_message = tracker.latest_message
            token = latest_message.get("metadata", {}).get("token")
            
            # TEMPORARY: Use hardcoded token for testing
            if not token:
                token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjI5MTQ4OTUsInVzZXJJZCI6IjEiLCJyb2xlSWQiOjEsImlhdCI6MTc2MDMyMjg5NX0.D_xKMtbNUH3BntCTmv5YWc6flDxFXT5XnckTW_3_fHg"
            
            if not token:
                # Fallback to mock data if no token
                dispatcher.utter_message(
                    text="Đây là các loại máy có sẵn:",
                    buttons=[
                        {"title": "Máy pin", "payload": "tôi muốn xem sản phẩm loại máy pin"},
                        {"title": "Máy cơ", "payload": "tôi muốn xem sản phẩm loại máy cơ"}
                    ]
                )
                return []

            # Call movement-types API with token
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }
            
            response = requests.get("http://localhost:8080/v1/movement-type", 
                                 headers=headers, timeout=10)
            response.raise_for_status()
            
            # Handle encoding issues
            response.encoding = 'utf-8'
            data = response.json()
            movement_types = data.get("movementTypes", {}).get("items", [])
            
            if not movement_types:
                dispatcher.utter_message(text="Hiện tại chưa có loại máy nào.")
                return []

            # Create buttons for each movement type
            buttons = []
            for movement_type in movement_types:
                movement_name = movement_type.get("name", "")
                movement_id = movement_type.get("id", "")
                buttons.append({
                    "title": movement_name,
                    "payload": f"tôi muốn xem đồng hồ loại máy {movement_name.lower()}",
                    "id": movement_id,
                    "metadata": {
                        "movement_type_id": movement_id,
                        "intent": "filter_products"
                    }
                })

            # Send message with buttons
            dispatcher.utter_message(
                text="Đây là các loại máy có sẵn:",
                buttons=buttons
            )

        except requests.exceptions.RequestException as e:
            # Fallback to mock data on API error
            dispatcher.utter_message(
                text="Đây là các loại máy có sẵn:",
                buttons=[
                    {"title": "Máy pin", "payload": "tôi muốn xem sản phẩm loại máy pin"},
                    {"title": "Máy cơ", "payload": "tôi muốn xem sản phẩm loại máy cơ"}
                ]
            )
        except Exception as e:
            dispatcher.utter_message(
                text="Có lỗi xảy ra khi tải thông tin loại máy."
            )

        return []


class ActionShowStrapMaterials(Action):
    """Action to fetch and display strap materials from API with JWT token"""

    def name(self) -> Text:
        return "action_show_strap_materials"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            # Get token from latest message metadata
            latest_message = tracker.latest_message
            token = latest_message.get("metadata", {}).get("token")
            
            if not token:
                # Fallback to mock data if no token
                dispatcher.utter_message(
                    text="Đây là các chất liệu dây đeo có sẵn:",
                    buttons=[
                        {"title": "Sắt", "payload": "tôi muốn xem sản phẩm chất liệu sắt"},
                        {"title": "Kim Cương", "payload": "tôi muốn xem sản phẩm chất liệu kim cương"}
                    ]
                )
                return []

            # Call strap materials API with token
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }
            
            response = requests.get("http://localhost:8080/v1/strap-materials", 
                                 headers=headers, timeout=10)
            response.raise_for_status()
            
            # Handle encoding issues
            response.encoding = 'utf-8'
            data = response.json()
            strap_materials = data.get("strapMaterials", {}).get("rows", [])
            
            if not strap_materials:
                dispatcher.utter_message(text="Hiện tại chưa có chất liệu dây đeo nào.")
                return []

            # Create buttons for each strap material
            buttons = []
            for material in strap_materials:
                material_name = material.get("name", "")
                material_id = material.get("id", "")
                buttons.append({
                    "title": material_name,
                    "payload": f"tôi muốn xem đồng hồ dây {material_name.lower()}",
                    "id": material_id,
                    "metadata": {
                        "material_id": material_id,
                        "intent": "filter_products"
                    }
                })

            # Send message with buttons
            dispatcher.utter_message(
                text="Đây là các chất liệu dây đeo có sẵn:",
                buttons=buttons
            )

        except requests.exceptions.RequestException as e:
            # Fallback to mock data on API error
            dispatcher.utter_message(
                text="Đây là các chất liệu dây đeo có sẵn:",
                buttons=[
                    {"title": "Sắt", "payload": "tôi muốn xem sản phẩm chất liệu sắt"},
                    {"title": "Kim Cương", "payload": "tôi muốn xem sản phẩm chất liệu kim cương"}
                ]
            )
        except Exception as e:
            dispatcher.utter_message(
                text="Có lỗi xảy ra khi tải thông tin chất liệu dây đeo."
            )

        return []


class ActionSearchProducts(Action):
    """Action to search products by query and return cards for FE"""

    def name(self) -> Text:
        return "action_search_products"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            # Get search query from user message
            latest_message = tracker.latest_message
            user_text = latest_message.get("text", "").lower()
            
            # Check if this is a button click with metadata
            metadata = latest_message.get("metadata", {})
            if metadata and any(k in metadata for k in [
                "brand_id", "category_id", "color_id", "movement_type_id", "material_id", "strap_material_id", "gender", "rating_min"
            ]):
                # This is a filter request from FE metadata (e.g., category_id), use filter action instead
                return ActionFilterProducts().run(dispatcher, tracker, domain)
            
            # Extract search terms from common patterns
            search_terms = []
            
            # Extract brand names
            brands = ["rolex", "casio", "dior", "masala", "omega", "tissot", "citizen"]
            for brand in brands:
                if brand in user_text:
                    search_terms.append(brand)
            
            # Extract category names  
            categories = ["nam", "nữ", "nam nữ", "học sinh", "sinh viên", "phú", "olympia12"]
            for category in categories:
                if category in user_text:
                    search_terms.append(category)
            
            # Extract color names
            colors = ["đen", "trắng", "vàng", "bạc", "xanh", "đỏ", "hồng", "tím", "cam", "nâu", "xám"]
            for color in colors:
                if color in user_text:
                    search_terms.append(color)
            
            # Extract material names
            materials = ["titan", "titanium", "sắt", "kim cương", "da", "nhựa", "cao su"]
            for material in materials:
                if material in user_text:
                    search_terms.append(material)
            
            # Extract movement types
            movements = ["máy pin", "máy cơ", "máy bền", "automatic", "quartz"]
            for movement in movements:
                if movement in user_text:
                    search_terms.append(movement)
            
            # If no specific terms found, use general search terms
            if not search_terms:
                if "đồng hồ" in user_text:
                    search_terms = ["đồng hồ"]
                else:
                    # Use the whole user text as search term
                    search_terms = [user_text.strip()]
            
            # Use the first search term
            search_query = search_terms[0] if search_terms else "đồng hồ"
            
            # Get token from latest message metadata
            token = latest_message.get("metadata", {}).get("token")
            
            headers = {"Content-Type": "application/json"}
            if token:
                headers["Authorization"] = f"Bearer {token}"
            
            # Call search API
            response = requests.get(f"http://localhost:8080/v1/search?page=1&limit=12&q={search_query}", 
                                 headers=headers, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            watches = data.get("watches", {}).get("items", [])
            
            if not watches:
                dispatcher.utter_message(text=f"Không tìm thấy sản phẩm nào với từ khóa '{search_query}'.")
                return []

            # Build cards payload for FE
            cards: List[Dict[str, Any]] = []
            for watch in watches:
                cards.append({
                    "id": watch.get("id"),
                    "code": watch.get("code"),
                    "name": watch.get("name"),
                    "description": watch.get("description"),
                    "model": watch.get("model"),
                    "caseMaterial": watch.get("case_material"),
                    "caseSize": watch.get("case_size"),
                    "strapSize": watch.get("strap_size"),
                    "gender": watch.get("gender"),
                    "waterResistance": watch.get("water_resistance"),
                    "releaseDate": watch.get("release_date"),
                    "sold": watch.get("sold"),
                    "basePrice": watch.get("base_price"),
                    "rating": watch.get("rating"),
                    "status": watch.get("status"),
                    "thumbnail": watch.get("thumbnail"),
                    "slider": (watch.get("slider") or "").split(",") if watch.get("slider") else [],
                    "brandId": watch.get("brand_id"),
                    "brandName": watch.get("brand_name"),
                    "categoryId": watch.get("category_id"),
                    "categoryName": watch.get("category_name"),
                    "movementTypeId": watch.get("movement_type_id"),
                    "movementTypeName": watch.get("movement_type_name"),
                    "createdAt": watch.get("created_at"),
                    "updatedAt": watch.get("updated_at")
                })

            dispatcher.utter_message(
                text=f"Đây là kết quả tìm kiếm cho '{search_query}':",
                custom={
                    "type": "cards",
                    "cards": cards
                }
            )

        except requests.exceptions.RequestException as e:
            # Fallback to mock cards on API error
            dispatcher.utter_message(
                text=f"Đây là kết quả tìm kiếm cho '{search_query}':",
                custom={
                    "type": "cards",
                    "cards": [
                        {
                            "id": "sample-search-1",
                            "code": "DH-SEARCH",
                            "name": "Đồng hồ tìm kiếm",
                            "description": "Kết quả tìm kiếm",
                            "model": "SEARCH",
                            "caseMaterial": "titan",
                            "caseSize": 40,
                            "strapSize": 20,
                            "gender": "0",
                            "waterResistance": "IP68",
                            "releaseDate": "2025-10-01",
                            "sold": 5,
                            "basePrice": 1500000,
                            "rating": 4,
                            "status": True,
                            "thumbnail": "https://via.placeholder.com/300x300",
                            "slider": [],
                            "brandId": "1",
                            "brandName": "Sample Brand",
                            "categoryId": "1",
                            "categoryName": "Sample Category",
                            "movementTypeId": "1",
                            "movementTypeName": "Sample Movement",
                            "createdAt": "20251017182236",
                            "updatedAt": None
                        }
                    ]
                }
            )
        except Exception as e:
            dispatcher.utter_message(
                text="Có lỗi xảy ra khi tìm kiếm sản phẩm."
            )

        return []


class ActionFilterProducts(Action):
    """Action to filter products by ID parameters and return cards for FE"""

    def name(self) -> Text:
        return "action_filter_products"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            # Get filter parameters from latest message metadata
            latest_message = tracker.latest_message
            metadata = latest_message.get("metadata", {})
            
            # Extract filter parameters
            brand_id = metadata.get("brand_id")
            category_id = metadata.get("category_id") 
            color_id = metadata.get("color_id")
            movement_type_id = metadata.get("movement_type_id")
            # Support both legacy material_id and the correct strap_material_id
            strap_material_id = metadata.get("strap_material_id") or metadata.get("material_id")
            gender = metadata.get("gender")
            rating_min = metadata.get("rating_min")
            
            # Get token from metadata
            token = metadata.get("token")
            
            headers = {"Content-Type": "application/json"}
            if token:
                headers["Authorization"] = f"Bearer {token}"
            
            # Build query parameters
            params = ["page=1", "limit=12"]
            
            if brand_id:
                params.append(f"brand_id__in={brand_id}")
            if category_id:
                params.append(f"category_id__in={category_id}")
            if color_id:
                params.append(f"color_id__in={color_id}")
            if movement_type_id:
                params.append(f"movement_type_id__in={movement_type_id}")
            if strap_material_id:
                params.append(f"strap_material_id__in={strap_material_id}")
            if gender is not None:
                params.append(f"gender__in={gender}")
            if rating_min is not None:
                params.append(f"rating__gte={rating_min}")
            
            query_string = "&".join(params)
            
            # Call search API with filter parameters
            response = requests.get(f"http://localhost:8080/v1/search?{query_string}", 
                                 headers=headers, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            watches = data.get("watches", {}).get("items", [])
            
            if not watches:
                dispatcher.utter_message(text="Không tìm thấy sản phẩm nào với bộ lọc này.")
                return []

            # Build cards payload for FE
            cards: List[Dict[str, Any]] = []
            for watch in watches:
                cards.append({
                    "id": watch.get("id"),
                    "code": watch.get("code"),
                    "name": watch.get("name"),
                    "description": watch.get("description"),
                    "model": watch.get("model"),
                    "caseMaterial": watch.get("case_material"),
                    "caseSize": watch.get("case_size"),
                    "strapSize": watch.get("strap_size"),
                    "gender": watch.get("gender"),
                    "waterResistance": watch.get("water_resistance"),
                    "releaseDate": watch.get("release_date"),
                    "sold": watch.get("sold"),
                    "basePrice": watch.get("base_price"),
                    "rating": watch.get("rating"),
                    "status": watch.get("status"),
                    "thumbnail": watch.get("thumbnail"),
                    "slider": (watch.get("slider") or "").split(",") if watch.get("slider") else [],
                    "brandId": watch.get("brand_id"),
                    "brandName": watch.get("brand_name"),
                    "categoryId": watch.get("category_id"),
                    "categoryName": watch.get("category_name"),
                    "movementTypeId": watch.get("movement_type_id"),
                    "movementTypeName": watch.get("movement_type_name"),
                    "createdAt": watch.get("created_at"),
                    "updatedAt": watch.get("updated_at")
                })

            # Create filter description with names instead of IDs
            # Try to resolve color name when color_id is provided
            color_name_resolved = None
            if color_id:
                # 1) Try to get from first watch result if available
                if watches:
                    color_name_resolved = watches[0].get("color_name") or None
                # 2) If not present, fetch colors list and map id -> name
                if not color_name_resolved:
                    try:
                        color_headers = {"Content-Type": "application/json"}
                        if token:
                            color_headers["Authorization"] = f"Bearer {token}"
                        colors_resp = requests.get("http://localhost:8080/v1/colors", headers=color_headers, timeout=10)
                        colors_resp.raise_for_status()
                        colors_data = colors_resp.json()
                        colors_items = colors_data.get("colors", {}).get("items", [])
                        for c in colors_items:
                            if str(c.get("id")) == str(color_id):
                                color_name_resolved = c.get("name")
                                break
                    except Exception:
                        pass

            # Try to resolve strap material name when material_id is provided
            material_name_resolved = None
            if strap_material_id:
                # 1) Try to get from first watch result if available
                if watches:
                    material_name_resolved = watches[0].get("strap_material_name") or watches[0].get("material_name") or None
                # 2) If not present, fetch strap-materials list and map id -> name
                if not material_name_resolved:
                    try:
                        sm_headers = {"Content-Type": "application/json"}
                        if token:
                            sm_headers["Authorization"] = f"Bearer {token}"
                        sm_resp = requests.get("http://localhost:8080/v1/strap-materials", headers=sm_headers, timeout=10)
                        sm_resp.raise_for_status()
                        sm_data = sm_resp.json()
                        sm_items = sm_data.get("strapMaterials", {}).get("rows", [])
                        for m in sm_items:
                            if str(m.get("id")) == str(strap_material_id):
                                material_name_resolved = m.get("name")
                                break
                    except Exception:
                        pass

            filter_desc = []
            if brand_id:
                # Try to get brand name from first watch result
                brand_name = watches[0].get("brand_name", f"ID {brand_id}") if watches else f"ID {brand_id}"
                filter_desc.append(f"thương hiệu {brand_name}")
            if category_id:
                category_name = watches[0].get("category_name", f"ID {category_id}") if watches else f"ID {category_id}"
                filter_desc.append(f"danh mục {category_name}")
            if color_id:
                if color_name_resolved:
                    filter_desc.append(f"màu sắc {color_name_resolved}")
                else:
                    filter_desc.append(f"màu sắc ID {color_id}")
            if movement_type_id:
                movement_name = watches[0].get("movement_type_name", f"ID {movement_type_id}") if watches else f"ID {movement_type_id}"
                filter_desc.append(f"loại máy {movement_name}")
            if strap_material_id:
                if material_name_resolved:
                    filter_desc.append(f"dây {material_name_resolved}")
                else:
                    filter_desc.append(f"dây ID {strap_material_id}")
            if gender is not None:
                gender_text = "nam" if gender == "0" else "nữ" if gender == "1" else f"{gender}"
                filter_desc.append(f"giới tính {gender_text}")
            if rating_min is not None:
                filter_desc.append(f"đánh giá từ {rating_min} sao")

            filter_text = ", ".join(filter_desc) if filter_desc else "bộ lọc"

            dispatcher.utter_message(
                text=f"Kết quả lọc theo {filter_text}:",
                custom={
                    "type": "cards",
                    "cards": cards
                }
            )

        except requests.exceptions.RequestException as e:
            # Fallback to mock cards on API error
            dispatcher.utter_message(
                text="Kết quả lọc sản phẩm:",
                custom={
                    "type": "cards",
                    "cards": [
                        {
                            "id": "sample-filter-1",
                            "code": "DH-FILTER",
                            "name": "Đồng hồ lọc",
                            "description": "Kết quả lọc",
                            "model": "FILTER",
                            "caseMaterial": "titan",
                            "caseSize": 40,
                            "strapSize": 20,
                            "gender": "0",
                            "waterResistance": "IP68",
                            "releaseDate": "2025-10-01",
                            "sold": 3,
                            "basePrice": 1800000,
                            "rating": 4,
                            "status": True,
                            "thumbnail": "https://via.placeholder.com/300x300",
                            "slider": [],
                            "brandId": "1",
                            "brandName": "Sample Brand",
                            "categoryId": "1",
                            "categoryName": "Sample Category",
                            "movementTypeId": "1",
                            "movementTypeName": "Sample Movement",
                            "createdAt": "20251017182236",
                            "updatedAt": None
                        }
                    ]
                }
            )
        except Exception as e:
            dispatcher.utter_message(
                text="Có lỗi xảy ra khi lọc sản phẩm."
            )

        return []


class ActionShowOrderStatus(Action):
    """Action to fetch and display order status information"""

    def name(self) -> Text:
        return "action_show_order_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            # Get token from latest message metadata
            latest_message = tracker.latest_message
            token = latest_message.get("metadata", {}).get("token")
            
            if not token:
                # Fallback message if no token
                dispatcher.utter_message(
                    text="Để xem tình trạng đơn hàng, bạn cần đăng nhập trước."
                )
                return []

            # Call orders API with token
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }
            
            # Fetch orders (limit 5)
            orders_response = requests.get("http://localhost:8080/v1/orders?limit=5", 
                                         headers=headers, timeout=10)
            orders_response.raise_for_status()
            
            # Fetch order statuses
            status_response = requests.get("http://localhost:8080/v1/order-status", 
                                         headers=headers, timeout=10)
            status_response.raise_for_status()
            
            orders_data = orders_response.json()
            status_data = status_response.json()
            
            orders = orders_data.get("orders", {}).get("items", [])
            order_statuses = status_data.get("orderStatuses", {}).get("rows", [])
            
            if not orders:
                dispatcher.utter_message(text="Bạn chưa có đơn hàng nào.")
                return []

            # Create status mapping for easy lookup
            status_map = {}
            for status in order_statuses:
                status_map[status.get("id")] = {
                    "name": status.get("name"),
                    "description": status.get("description"),
                    "color": status.get("color"),
                    "hex_code": status.get("hex_code")
                }

            # Create order cards with buttons
            order_cards = []
            for order in orders:
                order_id = order.get("id")
                order_code = order.get("code")
                total_amount = order.get("total_amount", 0)
                final_amount = order.get("final_amount", 0)
                current_status_id = order.get("current_status_id")
                created_at = order.get("created_at")
                guess_name = order.get("guess_name", "")
                
                # Get status info
                status_info = status_map.get(current_status_id, {})
                status_name = status_info.get("name", "Không xác định")
                status_color = status_info.get("color", "Gray")
                
                # Format amount
                formatted_amount = f"{final_amount:,}".replace(",", ".") + " VNĐ"
                
                # Format date
                formatted_date = created_at[:4] + "-" + created_at[4:6] + "-" + created_at[6:8] if created_at else "N/A"
                
                order_card = {
                    "id": order_id,
                    "code": order_code,
                    "customer_name": guess_name,
                    "total_amount": formatted_amount,
                    "status": status_name,
                    "status_color": status_color,
                    "created_date": formatted_date,
                    "buttons": [
                        {
                            "title": f"#{order_id} - {order_code} - {status_name}",
                            "payload": f"xem chi tiết đơn hàng {order_code}",
                            "metadata": {
                                "order_id": order_id,
                                "order_code": order_code,
                                "status_name": status_name,
                                "status_color": status_color,
                                "intent": "view_order_detail"
                            }
                        }
                    ]
                }
                order_cards.append(order_card)

            # Send message with order cards
            dispatcher.utter_message(
                text="Đây là danh sách đơn hàng của bạn:",
                custom={
                    "type": "order_cards",
                    "orders": order_cards
                }
            )

        except requests.exceptions.RequestException as e:
            # Fallback message on API error
            dispatcher.utter_message(
                text="Không thể tải thông tin đơn hàng. Vui lòng thử lại sau."
            )
        except Exception as e:
            dispatcher.utter_message(
                text="Có lỗi xảy ra khi tải thông tin đơn hàng."
            )

        return []


class ActionShowOrderStatuses(Action):
    """Action to fetch and display available order statuses"""

    def name(self) -> Text:
        return "action_show_order_statuses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            # Get token from latest message metadata
            latest_message = tracker.latest_message
            token = latest_message.get("metadata", {}).get("token")
            
            if not token:
                # Fallback message if no token
                dispatcher.utter_message(
                    text="Để xem trạng thái đơn hàng, bạn cần đăng nhập trước."
                )
                return []

            # Call order-status API with token
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }
            
            response = requests.get("http://localhost:8080/v1/order-status", 
                                 headers=headers, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            order_statuses = data.get("orderStatuses", {}).get("rows", [])
            
            if not order_statuses:
                dispatcher.utter_message(text="Hiện tại chưa có trạng thái đơn hàng nào.")
                return []

            # Create buttons for each status
            buttons = []
            for status in order_statuses:
                status_name = status.get("name", "")
                status_id = status.get("id", "")
                status_description = status.get("description", "")
                status_color = status.get("color", "")
                
                buttons.append({
                    "title": f"{status_name} ({status_color})",
                    "payload": f"xem đơn hàng trạng thái {status_name.lower()}",
                    "metadata": {
                        "status_id": status_id,
                        "status_name": status_name,
                        "status_description": status_description,
                        "status_color": status_color,
                        "intent": "filter_orders_by_status"
                    }
                })

            # Send message with buttons
            dispatcher.utter_message(
                text="Đây là các trạng thái đơn hàng có sẵn:",
                buttons=buttons
            )

        except requests.exceptions.RequestException as e:
            # Fallback message on API error
            dispatcher.utter_message(
                text="Không thể tải thông tin trạng thái đơn hàng. Vui lòng thử lại sau."
            )
        except Exception as e:
            dispatcher.utter_message(
                text="Có lỗi xảy ra khi tải thông tin trạng thái đơn hàng."
            )

        return []


class ActionShowPromotions(Action):
    """Action to fetch and display promotions/discounts from API"""

    def name(self) -> Text:
        return "action_show_promotions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            # Get token from latest message metadata
            latest_message = tracker.latest_message
            token = latest_message.get("metadata", {}).get("token")
            
            if not token:
                # Fallback message if no token
                dispatcher.utter_message(
                    text="Để xem khuyến mãi, bạn cần đăng nhập trước."
                )
                return []

            # Call discounts API with token
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }
            
            response = requests.get("http://localhost:8080/v1/discounts", 
                                 headers=headers, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            discounts = data.get("discounts", {}).get("items", [])
            
            if not discounts:
                dispatcher.utter_message(text="Hiện tại chưa có khuyến mãi nào.")
                return []

            # Create promotion cards
            promotion_cards = []
            for discount in discounts:
                discount_id = discount.get("id")
                discount_code = discount.get("code")
                discount_name = discount.get("name")
                description = discount.get("description")
                min_order_value = discount.get("min_order_value", 0)
                max_discount_amount = discount.get("max_discount_amount", 0)
                discount_type = discount.get("discount_type")
                discount_value = discount.get("discount_value", 0)
                effective_date = discount.get("effective_date")
                valid_until = discount.get("valid_until")
                
                # Format amounts
                formatted_min_order = f"{min_order_value:,}".replace(",", ".") + " VNĐ"
                formatted_max_discount = f"{max_discount_amount:,}".replace(",", ".") + " VNĐ"
                
                # Format discount value based on type
                if discount_type == "0":  # Fixed amount
                    formatted_discount_value = f"{discount_value:,}".replace(",", ".") + " VNĐ"
                else:  # Percentage
                    formatted_discount_value = f"{discount_value}%"
                
                # Format dates
                formatted_effective_date = effective_date[:4] + "-" + effective_date[4:6] + "-" + effective_date[6:8] if effective_date else "N/A"
                formatted_valid_until = valid_until[:4] + "-" + valid_until[4:6] + "-" + valid_until[6:8] if valid_until else "N/A"
                
                promotion_card = {
                    "id": discount_id,
                    "code": discount_code,
                    "name": discount_name,
                    "description": description,
                    "discount_value": formatted_discount_value,
                    "min_order_value": formatted_min_order,
                    "max_discount_amount": formatted_max_discount,
                    "effective_date": formatted_effective_date,
                    "valid_until": formatted_valid_until,
                    "discount_type": "Giảm cố định" if discount_type == "0" else "Giảm phần trăm"
                }
                promotion_cards.append(promotion_card)

            # Send message with promotion cards
            dispatcher.utter_message(
                text="Đây là các chương trình khuyến mãi hiện tại:",
                custom={
                    "type": "promotion_cards",
                    "promotions": promotion_cards
                }
            )

        except requests.exceptions.RequestException as e:
            # Fallback message on API error
            dispatcher.utter_message(
                text="Không thể tải thông tin khuyến mãi. Vui lòng thử lại sau."
            )
        except Exception as e:
            dispatcher.utter_message(
                text="Có lỗi xảy ra khi tải thông tin khuyến mãi."
            )

        return []