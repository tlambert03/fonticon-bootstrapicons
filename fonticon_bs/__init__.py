__all__ = ["Bootstrap"]
__version__ = "1.5.0"

from pathlib import Path
from enum import Enum


class Bootstrap(Enum):
    @classmethod
    def _font_file(self) -> str:
        fonts = Path(__file__).parent / "fonts"
        return str(fonts / "bootstrap-icons.otf")

    alarm_fill = "\uf101"
    alarm = "\uf102"
    align_bottom = "\uf103"
    align_center = "\uf104"
    align_end = "\uf105"
    align_middle = "\uf106"
    align_start = "\uf107"
    align_top = "\uf108"
    alt = "\uf109"
    app_indicator = "\uf10a"
    app = "\uf10b"
    archive_fill = "\uf10c"
    archive = "\uf10d"
    arrow_90deg_down = "\uf10e"
    arrow_90deg_left = "\uf10f"
    arrow_90deg_right = "\uf110"
    arrow_90deg_up = "\uf111"
    arrow_bar_down = "\uf112"
    arrow_bar_left = "\uf113"
    arrow_bar_right = "\uf114"
    arrow_bar_up = "\uf115"
    arrow_clockwise = "\uf116"
    arrow_counterclockwise = "\uf117"
    arrow_down_circle_fill = "\uf118"
    arrow_down_circle = "\uf119"
    arrow_down_left_circle_fill = "\uf11a"
    arrow_down_left_circle = "\uf11b"
    arrow_down_left_square_fill = "\uf11c"
    arrow_down_left_square = "\uf11d"
    arrow_down_left = "\uf11e"
    arrow_down_right_circle_fill = "\uf11f"
    arrow_down_right_circle = "\uf120"
    arrow_down_right_square_fill = "\uf121"
    arrow_down_right_square = "\uf122"
    arrow_down_right = "\uf123"
    arrow_down_short = "\uf124"
    arrow_down_square_fill = "\uf125"
    arrow_down_square = "\uf126"
    arrow_down_up = "\uf127"
    arrow_down = "\uf128"
    arrow_left_circle_fill = "\uf129"
    arrow_left_circle = "\uf12a"
    arrow_left_right = "\uf12b"
    arrow_left_short = "\uf12c"
    arrow_left_square_fill = "\uf12d"
    arrow_left_square = "\uf12e"
    arrow_left = "\uf12f"
    arrow_repeat = "\uf130"
    arrow_return_left = "\uf131"
    arrow_return_right = "\uf132"
    arrow_right_circle_fill = "\uf133"
    arrow_right_circle = "\uf134"
    arrow_right_short = "\uf135"
    arrow_right_square_fill = "\uf136"
    arrow_right_square = "\uf137"
    arrow_right = "\uf138"
    arrow_up_circle_fill = "\uf139"
    arrow_up_circle = "\uf13a"
    arrow_up_left_circle_fill = "\uf13b"
    arrow_up_left_circle = "\uf13c"
    arrow_up_left_square_fill = "\uf13d"
    arrow_up_left_square = "\uf13e"
    arrow_up_left = "\uf13f"
    arrow_up_right_circle_fill = "\uf140"
    arrow_up_right_circle = "\uf141"
    arrow_up_right_square_fill = "\uf142"
    arrow_up_right_square = "\uf143"
    arrow_up_right = "\uf144"
    arrow_up_short = "\uf145"
    arrow_up_square_fill = "\uf146"
    arrow_up_square = "\uf147"
    arrow_up = "\uf148"
    arrows_angle_contract = "\uf149"
    arrows_angle_expand = "\uf14a"
    arrows_collapse = "\uf14b"
    arrows_expand = "\uf14c"
    arrows_fullscreen = "\uf14d"
    arrows_move = "\uf14e"
    aspect_ratio_fill = "\uf14f"
    aspect_ratio = "\uf150"
    asterisk = "\uf151"
    at = "\uf152"
    award_fill = "\uf153"
    award = "\uf154"
    back = "\uf155"
    backspace_fill = "\uf156"
    backspace_reverse_fill = "\uf157"
    backspace_reverse = "\uf158"
    backspace = "\uf159"
    badge_3d_fill = "\uf15a"
    badge_3d = "\uf15b"
    badge_4k_fill = "\uf15c"
    badge_4k = "\uf15d"
    badge_8k_fill = "\uf15e"
    badge_8k = "\uf15f"
    badge_ad_fill = "\uf160"
    badge_ad = "\uf161"
    badge_ar_fill = "\uf162"
    badge_ar = "\uf163"
    badge_cc_fill = "\uf164"
    badge_cc = "\uf165"
    badge_hd_fill = "\uf166"
    badge_hd = "\uf167"
    badge_tm_fill = "\uf168"
    badge_tm = "\uf169"
    badge_vo_fill = "\uf16a"
    badge_vo = "\uf16b"
    badge_vr_fill = "\uf16c"
    badge_vr = "\uf16d"
    badge_wc_fill = "\uf16e"
    badge_wc = "\uf16f"
    bag_check_fill = "\uf170"
    bag_check = "\uf171"
    bag_dash_fill = "\uf172"
    bag_dash = "\uf173"
    bag_fill = "\uf174"
    bag_plus_fill = "\uf175"
    bag_plus = "\uf176"
    bag_x_fill = "\uf177"
    bag_x = "\uf178"
    bag = "\uf179"
    bar_chart_fill = "\uf17a"
    bar_chart_line_fill = "\uf17b"
    bar_chart_line = "\uf17c"
    bar_chart_steps = "\uf17d"
    bar_chart = "\uf17e"
    basket_fill = "\uf17f"
    basket = "\uf180"
    basket2_fill = "\uf181"
    basket2 = "\uf182"
    basket3_fill = "\uf183"
    basket3 = "\uf184"
    battery_charging = "\uf185"
    battery_full = "\uf186"
    battery_half = "\uf187"
    battery = "\uf188"
    bell_fill = "\uf189"
    bell = "\uf18a"
    bezier = "\uf18b"
    bezier2 = "\uf18c"
    bicycle = "\uf18d"
    binoculars_fill = "\uf18e"
    binoculars = "\uf18f"
    blockquote_left = "\uf190"
    blockquote_right = "\uf191"
    book_fill = "\uf192"
    book_half = "\uf193"
    book = "\uf194"
    bookmark_check_fill = "\uf195"
    bookmark_check = "\uf196"
    bookmark_dash_fill = "\uf197"
    bookmark_dash = "\uf198"
    bookmark_fill = "\uf199"
    bookmark_heart_fill = "\uf19a"
    bookmark_heart = "\uf19b"
    bookmark_plus_fill = "\uf19c"
    bookmark_plus = "\uf19d"
    bookmark_star_fill = "\uf19e"
    bookmark_star = "\uf19f"
    bookmark_x_fill = "\uf1a0"
    bookmark_x = "\uf1a1"
    bookmark = "\uf1a2"
    bookmarks_fill = "\uf1a3"
    bookmarks = "\uf1a4"
    bookshelf = "\uf1a5"
    bootstrap_fill = "\uf1a6"
    bootstrap_reboot = "\uf1a7"
    bootstrap = "\uf1a8"
    border_all = "\uf1a9"
    border_bottom = "\uf1aa"
    border_center = "\uf1ab"
    border_inner = "\uf1ac"
    border_left = "\uf1ad"
    border_middle = "\uf1ae"
    border_outer = "\uf1af"
    border_right = "\uf1b0"
    border_style = "\uf1b1"
    border_top = "\uf1b2"
    border_width = "\uf1b3"
    border = "\uf1b4"
    bounding_box_circles = "\uf1b5"
    bounding_box = "\uf1b6"
    box_arrow_down_left = "\uf1b7"
    box_arrow_down_right = "\uf1b8"
    box_arrow_down = "\uf1b9"
    box_arrow_in_down_left = "\uf1ba"
    box_arrow_in_down_right = "\uf1bb"
    box_arrow_in_down = "\uf1bc"
    box_arrow_in_left = "\uf1bd"
    box_arrow_in_right = "\uf1be"
    box_arrow_in_up_left = "\uf1bf"
    box_arrow_in_up_right = "\uf1c0"
    box_arrow_in_up = "\uf1c1"
    box_arrow_left = "\uf1c2"
    box_arrow_right = "\uf1c3"
    box_arrow_up_left = "\uf1c4"
    box_arrow_up_right = "\uf1c5"
    box_arrow_up = "\uf1c6"
    box_seam = "\uf1c7"
    box = "\uf1c8"
    braces = "\uf1c9"
    bricks = "\uf1ca"
    briefcase_fill = "\uf1cb"
    briefcase = "\uf1cc"
    brightness_alt_high_fill = "\uf1cd"
    brightness_alt_high = "\uf1ce"
    brightness_alt_low_fill = "\uf1cf"
    brightness_alt_low = "\uf1d0"
    brightness_high_fill = "\uf1d1"
    brightness_high = "\uf1d2"
    brightness_low_fill = "\uf1d3"
    brightness_low = "\uf1d4"
    broadcast_pin = "\uf1d5"
    broadcast = "\uf1d6"
    brush_fill = "\uf1d7"
    brush = "\uf1d8"
    bucket_fill = "\uf1d9"
    bucket = "\uf1da"
    bug_fill = "\uf1db"
    bug = "\uf1dc"
    building = "\uf1dd"
    bullseye = "\uf1de"
    calculator_fill = "\uf1df"
    calculator = "\uf1e0"
    calendar_check_fill = "\uf1e1"
    calendar_check = "\uf1e2"
    calendar_date_fill = "\uf1e3"
    calendar_date = "\uf1e4"
    calendar_day_fill = "\uf1e5"
    calendar_day = "\uf1e6"
    calendar_event_fill = "\uf1e7"
    calendar_event = "\uf1e8"
    calendar_fill = "\uf1e9"
    calendar_minus_fill = "\uf1ea"
    calendar_minus = "\uf1eb"
    calendar_month_fill = "\uf1ec"
    calendar_month = "\uf1ed"
    calendar_plus_fill = "\uf1ee"
    calendar_plus = "\uf1ef"
    calendar_range_fill = "\uf1f0"
    calendar_range = "\uf1f1"
    calendar_week_fill = "\uf1f2"
    calendar_week = "\uf1f3"
    calendar_x_fill = "\uf1f4"
    calendar_x = "\uf1f5"
    calendar = "\uf1f6"
    calendar2_check_fill = "\uf1f7"
    calendar2_check = "\uf1f8"
    calendar2_date_fill = "\uf1f9"
    calendar2_date = "\uf1fa"
    calendar2_day_fill = "\uf1fb"
    calendar2_day = "\uf1fc"
    calendar2_event_fill = "\uf1fd"
    calendar2_event = "\uf1fe"
    calendar2_fill = "\uf1ff"
    calendar2_minus_fill = "\uf200"
    calendar2_minus = "\uf201"
    calendar2_month_fill = "\uf202"
    calendar2_month = "\uf203"
    calendar2_plus_fill = "\uf204"
    calendar2_plus = "\uf205"
    calendar2_range_fill = "\uf206"
    calendar2_range = "\uf207"
    calendar2_week_fill = "\uf208"
    calendar2_week = "\uf209"
    calendar2_x_fill = "\uf20a"
    calendar2_x = "\uf20b"
    calendar2 = "\uf20c"
    calendar3_event_fill = "\uf20d"
    calendar3_event = "\uf20e"
    calendar3_fill = "\uf20f"
    calendar3_range_fill = "\uf210"
    calendar3_range = "\uf211"
    calendar3_week_fill = "\uf212"
    calendar3_week = "\uf213"
    calendar3 = "\uf214"
    calendar4_event = "\uf215"
    calendar4_range = "\uf216"
    calendar4_week = "\uf217"
    calendar4 = "\uf218"
    camera_fill = "\uf219"
    camera_reels_fill = "\uf21a"
    camera_reels = "\uf21b"
    camera_video_fill = "\uf21c"
    camera_video_off_fill = "\uf21d"
    camera_video_off = "\uf21e"
    camera_video = "\uf21f"
    camera = "\uf220"
    camera2 = "\uf221"
    capslock_fill = "\uf222"
    capslock = "\uf223"
    card_checklist = "\uf224"
    card_heading = "\uf225"
    card_image = "\uf226"
    card_list = "\uf227"
    card_text = "\uf228"
    caret_down_fill = "\uf229"
    caret_down_square_fill = "\uf22a"
    caret_down_square = "\uf22b"
    caret_down = "\uf22c"
    caret_left_fill = "\uf22d"
    caret_left_square_fill = "\uf22e"
    caret_left_square = "\uf22f"
    caret_left = "\uf230"
    caret_right_fill = "\uf231"
    caret_right_square_fill = "\uf232"
    caret_right_square = "\uf233"
    caret_right = "\uf234"
    caret_up_fill = "\uf235"
    caret_up_square_fill = "\uf236"
    caret_up_square = "\uf237"
    caret_up = "\uf238"
    cart_check_fill = "\uf239"
    cart_check = "\uf23a"
    cart_dash_fill = "\uf23b"
    cart_dash = "\uf23c"
    cart_fill = "\uf23d"
    cart_plus_fill = "\uf23e"
    cart_plus = "\uf23f"
    cart_x_fill = "\uf240"
    cart_x = "\uf241"
    cart = "\uf242"
    cart2 = "\uf243"
    cart3 = "\uf244"
    cart4 = "\uf245"
    cash_stack = "\uf246"
    cash = "\uf247"
    cast = "\uf248"
    chat_dots_fill = "\uf249"
    chat_dots = "\uf24a"
    chat_fill = "\uf24b"
    chat_left_dots_fill = "\uf24c"
    chat_left_dots = "\uf24d"
    chat_left_fill = "\uf24e"
    chat_left_quote_fill = "\uf24f"
    chat_left_quote = "\uf250"
    chat_left_text_fill = "\uf251"
    chat_left_text = "\uf252"
    chat_left = "\uf253"
    chat_quote_fill = "\uf254"
    chat_quote = "\uf255"
    chat_right_dots_fill = "\uf256"
    chat_right_dots = "\uf257"
    chat_right_fill = "\uf258"
    chat_right_quote_fill = "\uf259"
    chat_right_quote = "\uf25a"
    chat_right_text_fill = "\uf25b"
    chat_right_text = "\uf25c"
    chat_right = "\uf25d"
    chat_square_dots_fill = "\uf25e"
    chat_square_dots = "\uf25f"
    chat_square_fill = "\uf260"
    chat_square_quote_fill = "\uf261"
    chat_square_quote = "\uf262"
    chat_square_text_fill = "\uf263"
    chat_square_text = "\uf264"
    chat_square = "\uf265"
    chat_text_fill = "\uf266"
    chat_text = "\uf267"
    chat = "\uf268"
    check_all = "\uf269"
    check_circle_fill = "\uf26a"
    check_circle = "\uf26b"
    check_square_fill = "\uf26c"
    check_square = "\uf26d"
    check = "\uf26e"
    check2_all = "\uf26f"
    check2_circle = "\uf270"
    check2_square = "\uf271"
    check2 = "\uf272"
    chevron_bar_contract = "\uf273"
    chevron_bar_down = "\uf274"
    chevron_bar_expand = "\uf275"
    chevron_bar_left = "\uf276"
    chevron_bar_right = "\uf277"
    chevron_bar_up = "\uf278"
    chevron_compact_down = "\uf279"
    chevron_compact_left = "\uf27a"
    chevron_compact_right = "\uf27b"
    chevron_compact_up = "\uf27c"
    chevron_contract = "\uf27d"
    chevron_double_down = "\uf27e"
    chevron_double_left = "\uf27f"
    chevron_double_right = "\uf280"
    chevron_double_up = "\uf281"
    chevron_down = "\uf282"
    chevron_expand = "\uf283"
    chevron_left = "\uf284"
    chevron_right = "\uf285"
    chevron_up = "\uf286"
    circle_fill = "\uf287"
    circle_half = "\uf288"
    circle_square = "\uf289"
    circle = "\uf28a"
    clipboard_check = "\uf28b"
    clipboard_data = "\uf28c"
    clipboard_minus = "\uf28d"
    clipboard_plus = "\uf28e"
    clipboard_x = "\uf28f"
    clipboard = "\uf290"
    clock_fill = "\uf291"
    clock_history = "\uf292"
    clock = "\uf293"
    cloud_arrow_down_fill = "\uf294"
    cloud_arrow_down = "\uf295"
    cloud_arrow_up_fill = "\uf296"
    cloud_arrow_up = "\uf297"
    cloud_check_fill = "\uf298"
    cloud_check = "\uf299"
    cloud_download_fill = "\uf29a"
    cloud_download = "\uf29b"
    cloud_drizzle_fill = "\uf29c"
    cloud_drizzle = "\uf29d"
    cloud_fill = "\uf29e"
    cloud_fog_fill = "\uf29f"
    cloud_fog = "\uf2a0"
    cloud_fog2_fill = "\uf2a1"
    cloud_fog2 = "\uf2a2"
    cloud_hail_fill = "\uf2a3"
    cloud_hail = "\uf2a4"
    cloud_haze_1 = "\uf2a5"
    cloud_haze_fill = "\uf2a6"
    cloud_haze = "\uf2a7"
    cloud_haze2_fill = "\uf2a8"
    cloud_lightning_fill = "\uf2a9"
    cloud_lightning_rain_fill = "\uf2aa"
    cloud_lightning_rain = "\uf2ab"
    cloud_lightning = "\uf2ac"
    cloud_minus_fill = "\uf2ad"
    cloud_minus = "\uf2ae"
    cloud_moon_fill = "\uf2af"
    cloud_moon = "\uf2b0"
    cloud_plus_fill = "\uf2b1"
    cloud_plus = "\uf2b2"
    cloud_rain_fill = "\uf2b3"
    cloud_rain_heavy_fill = "\uf2b4"
    cloud_rain_heavy = "\uf2b5"
    cloud_rain = "\uf2b6"
    cloud_slash_fill = "\uf2b7"
    cloud_slash = "\uf2b8"
    cloud_sleet_fill = "\uf2b9"
    cloud_sleet = "\uf2ba"
    cloud_snow_fill = "\uf2bb"
    cloud_snow = "\uf2bc"
    cloud_sun_fill = "\uf2bd"
    cloud_sun = "\uf2be"
    cloud_upload_fill = "\uf2bf"
    cloud_upload = "\uf2c0"
    cloud = "\uf2c1"
    clouds_fill = "\uf2c2"
    clouds = "\uf2c3"
    cloudy_fill = "\uf2c4"
    cloudy = "\uf2c5"
    code_slash = "\uf2c6"
    code_square = "\uf2c7"
    code = "\uf2c8"
    collection_fill = "\uf2c9"
    collection_play_fill = "\uf2ca"
    collection_play = "\uf2cb"
    collection = "\uf2cc"
    columns_gap = "\uf2cd"
    columns = "\uf2ce"
    command = "\uf2cf"
    compass_fill = "\uf2d0"
    compass = "\uf2d1"
    cone_striped = "\uf2d2"
    cone = "\uf2d3"
    controller = "\uf2d4"
    cpu_fill = "\uf2d5"
    cpu = "\uf2d6"
    credit_card_2_back_fill = "\uf2d7"
    credit_card_2_back = "\uf2d8"
    credit_card_2_front_fill = "\uf2d9"
    credit_card_2_front = "\uf2da"
    credit_card_fill = "\uf2db"
    credit_card = "\uf2dc"
    crop = "\uf2dd"
    cup_fill = "\uf2de"
    cup_straw = "\uf2df"
    cup = "\uf2e0"
    cursor_fill = "\uf2e1"
    cursor_text = "\uf2e2"
    cursor = "\uf2e3"
    dash_circle_dotted = "\uf2e4"
    dash_circle_fill = "\uf2e5"
    dash_circle = "\uf2e6"
    dash_square_dotted = "\uf2e7"
    dash_square_fill = "\uf2e8"
    dash_square = "\uf2e9"
    dash = "\uf2ea"
    diagram_2_fill = "\uf2eb"
    diagram_2 = "\uf2ec"
    diagram_3_fill = "\uf2ed"
    diagram_3 = "\uf2ee"
    diamond_fill = "\uf2ef"
    diamond_half = "\uf2f0"
    diamond = "\uf2f1"
    dice_1_fill = "\uf2f2"
    dice_1 = "\uf2f3"
    dice_2_fill = "\uf2f4"
    dice_2 = "\uf2f5"
    dice_3_fill = "\uf2f6"
    dice_3 = "\uf2f7"
    dice_4_fill = "\uf2f8"
    dice_4 = "\uf2f9"
    dice_5_fill = "\uf2fa"
    dice_5 = "\uf2fb"
    dice_6_fill = "\uf2fc"
    dice_6 = "\uf2fd"
    disc_fill = "\uf2fe"
    disc = "\uf2ff"
    discord = "\uf300"
    display_fill = "\uf301"
    display = "\uf302"
    distribute_horizontal = "\uf303"
    distribute_vertical = "\uf304"
    door_closed_fill = "\uf305"
    door_closed = "\uf306"
    door_open_fill = "\uf307"
    door_open = "\uf308"
    dot = "\uf309"
    download = "\uf30a"
    droplet_fill = "\uf30b"
    droplet_half = "\uf30c"
    droplet = "\uf30d"
    earbuds = "\uf30e"
    easel_fill = "\uf30f"
    easel = "\uf310"
    egg_fill = "\uf311"
    egg_fried = "\uf312"
    egg = "\uf313"
    eject_fill = "\uf314"
    eject = "\uf315"
    emoji_angry_fill = "\uf316"
    emoji_angry = "\uf317"
    emoji_dizzy_fill = "\uf318"
    emoji_dizzy = "\uf319"
    emoji_expressionless_fill = "\uf31a"
    emoji_expressionless = "\uf31b"
    emoji_frown_fill = "\uf31c"
    emoji_frown = "\uf31d"
    emoji_heart_eyes_fill = "\uf31e"
    emoji_heart_eyes = "\uf31f"
    emoji_laughing_fill = "\uf320"
    emoji_laughing = "\uf321"
    emoji_neutral_fill = "\uf322"
    emoji_neutral = "\uf323"
    emoji_smile_fill = "\uf324"
    emoji_smile_upside_down_fill = "\uf325"
    emoji_smile_upside_down = "\uf326"
    emoji_smile = "\uf327"
    emoji_sunglasses_fill = "\uf328"
    emoji_sunglasses = "\uf329"
    emoji_wink_fill = "\uf32a"
    emoji_wink = "\uf32b"
    envelope_fill = "\uf32c"
    envelope_open_fill = "\uf32d"
    envelope_open = "\uf32e"
    envelope = "\uf32f"
    eraser_fill = "\uf330"
    eraser = "\uf331"
    exclamation_circle_fill = "\uf332"
    exclamation_circle = "\uf333"
    exclamation_diamond_fill = "\uf334"
    exclamation_diamond = "\uf335"
    exclamation_octagon_fill = "\uf336"
    exclamation_octagon = "\uf337"
    exclamation_square_fill = "\uf338"
    exclamation_square = "\uf339"
    exclamation_triangle_fill = "\uf33a"
    exclamation_triangle = "\uf33b"
    exclamation = "\uf33c"
    exclude = "\uf33d"
    eye_fill = "\uf33e"
    eye_slash_fill = "\uf33f"
    eye_slash = "\uf340"
    eye = "\uf341"
    eyedropper = "\uf342"
    eyeglasses = "\uf343"
    facebook = "\uf344"
    file_arrow_down_fill = "\uf345"
    file_arrow_down = "\uf346"
    file_arrow_up_fill = "\uf347"
    file_arrow_up = "\uf348"
    file_bar_graph_fill = "\uf349"
    file_bar_graph = "\uf34a"
    file_binary_fill = "\uf34b"
    file_binary = "\uf34c"
    file_break_fill = "\uf34d"
    file_break = "\uf34e"
    file_check_fill = "\uf34f"
    file_check = "\uf350"
    file_code_fill = "\uf351"
    file_code = "\uf352"
    file_diff_fill = "\uf353"
    file_diff = "\uf354"
    file_earmark_arrow_down_fill = "\uf355"
    file_earmark_arrow_down = "\uf356"
    file_earmark_arrow_up_fill = "\uf357"
    file_earmark_arrow_up = "\uf358"
    file_earmark_bar_graph_fill = "\uf359"
    file_earmark_bar_graph = "\uf35a"
    file_earmark_binary_fill = "\uf35b"
    file_earmark_binary = "\uf35c"
    file_earmark_break_fill = "\uf35d"
    file_earmark_break = "\uf35e"
    file_earmark_check_fill = "\uf35f"
    file_earmark_check = "\uf360"
    file_earmark_code_fill = "\uf361"
    file_earmark_code = "\uf362"
    file_earmark_diff_fill = "\uf363"
    file_earmark_diff = "\uf364"
    file_earmark_easel_fill = "\uf365"
    file_earmark_easel = "\uf366"
    file_earmark_excel_fill = "\uf367"
    file_earmark_excel = "\uf368"
    file_earmark_fill = "\uf369"
    file_earmark_font_fill = "\uf36a"
    file_earmark_font = "\uf36b"
    file_earmark_image_fill = "\uf36c"
    file_earmark_image = "\uf36d"
    file_earmark_lock_fill = "\uf36e"
    file_earmark_lock = "\uf36f"
    file_earmark_lock2_fill = "\uf370"
    file_earmark_lock2 = "\uf371"
    file_earmark_medical_fill = "\uf372"
    file_earmark_medical = "\uf373"
    file_earmark_minus_fill = "\uf374"
    file_earmark_minus = "\uf375"
    file_earmark_music_fill = "\uf376"
    file_earmark_music = "\uf377"
    file_earmark_person_fill = "\uf378"
    file_earmark_person = "\uf379"
    file_earmark_play_fill = "\uf37a"
    file_earmark_play = "\uf37b"
    file_earmark_plus_fill = "\uf37c"
    file_earmark_plus = "\uf37d"
    file_earmark_post_fill = "\uf37e"
    file_earmark_post = "\uf37f"
    file_earmark_ppt_fill = "\uf380"
    file_earmark_ppt = "\uf381"
    file_earmark_richtext_fill = "\uf382"
    file_earmark_richtext = "\uf383"
    file_earmark_ruled_fill = "\uf384"
    file_earmark_ruled = "\uf385"
    file_earmark_slides_fill = "\uf386"
    file_earmark_slides = "\uf387"
    file_earmark_spreadsheet_fill = "\uf388"
    file_earmark_spreadsheet = "\uf389"
    file_earmark_text_fill = "\uf38a"
    file_earmark_text = "\uf38b"
    file_earmark_word_fill = "\uf38c"
    file_earmark_word = "\uf38d"
    file_earmark_x_fill = "\uf38e"
    file_earmark_x = "\uf38f"
    file_earmark_zip_fill = "\uf390"
    file_earmark_zip = "\uf391"
    file_earmark = "\uf392"
    file_easel_fill = "\uf393"
    file_easel = "\uf394"
    file_excel_fill = "\uf395"
    file_excel = "\uf396"
    file_fill = "\uf397"
    file_font_fill = "\uf398"
    file_font = "\uf399"
    file_image_fill = "\uf39a"
    file_image = "\uf39b"
    file_lock_fill = "\uf39c"
    file_lock = "\uf39d"
    file_lock2_fill = "\uf39e"
    file_lock2 = "\uf39f"
    file_medical_fill = "\uf3a0"
    file_medical = "\uf3a1"
    file_minus_fill = "\uf3a2"
    file_minus = "\uf3a3"
    file_music_fill = "\uf3a4"
    file_music = "\uf3a5"
    file_person_fill = "\uf3a6"
    file_person = "\uf3a7"
    file_play_fill = "\uf3a8"
    file_play = "\uf3a9"
    file_plus_fill = "\uf3aa"
    file_plus = "\uf3ab"
    file_post_fill = "\uf3ac"
    file_post = "\uf3ad"
    file_ppt_fill = "\uf3ae"
    file_ppt = "\uf3af"
    file_richtext_fill = "\uf3b0"
    file_richtext = "\uf3b1"
    file_ruled_fill = "\uf3b2"
    file_ruled = "\uf3b3"
    file_slides_fill = "\uf3b4"
    file_slides = "\uf3b5"
    file_spreadsheet_fill = "\uf3b6"
    file_spreadsheet = "\uf3b7"
    file_text_fill = "\uf3b8"
    file_text = "\uf3b9"
    file_word_fill = "\uf3ba"
    file_word = "\uf3bb"
    file_x_fill = "\uf3bc"
    file_x = "\uf3bd"
    file_zip_fill = "\uf3be"
    file_zip = "\uf3bf"
    file = "\uf3c0"
    files_alt = "\uf3c1"
    files = "\uf3c2"
    film = "\uf3c3"
    filter_circle_fill = "\uf3c4"
    filter_circle = "\uf3c5"
    filter_left = "\uf3c6"
    filter_right = "\uf3c7"
    filter_square_fill = "\uf3c8"
    filter_square = "\uf3c9"
    filter = "\uf3ca"
    flag_fill = "\uf3cb"
    flag = "\uf3cc"
    flower1 = "\uf3cd"
    flower2 = "\uf3ce"
    flower3 = "\uf3cf"
    folder_check = "\uf3d0"
    folder_fill = "\uf3d1"
    folder_minus = "\uf3d2"
    folder_plus = "\uf3d3"
    folder_symlink_fill = "\uf3d4"
    folder_symlink = "\uf3d5"
    folder_x = "\uf3d6"
    folder = "\uf3d7"
    folder2_open = "\uf3d8"
    folder2 = "\uf3d9"
    fonts = "\uf3da"
    forward_fill = "\uf3db"
    forward = "\uf3dc"
    front = "\uf3dd"
    fullscreen_exit = "\uf3de"
    fullscreen = "\uf3df"
    funnel_fill = "\uf3e0"
    funnel = "\uf3e1"
    gear_fill = "\uf3e2"
    gear_wide_connected = "\uf3e3"
    gear_wide = "\uf3e4"
    gear = "\uf3e5"
    gem = "\uf3e6"
    geo_alt_fill = "\uf3e7"
    geo_alt = "\uf3e8"
    geo_fill = "\uf3e9"
    geo = "\uf3ea"
    gift_fill = "\uf3eb"
    gift = "\uf3ec"
    github = "\uf3ed"
    globe = "\uf3ee"
    globe2 = "\uf3ef"
    google = "\uf3f0"
    graph_down = "\uf3f1"
    graph_up = "\uf3f2"
    grid_1x2_fill = "\uf3f3"
    grid_1x2 = "\uf3f4"
    grid_3x2_gap_fill = "\uf3f5"
    grid_3x2_gap = "\uf3f6"
    grid_3x2 = "\uf3f7"
    grid_3x3_gap_fill = "\uf3f8"
    grid_3x3_gap = "\uf3f9"
    grid_3x3 = "\uf3fa"
    grid_fill = "\uf3fb"
    grid = "\uf3fc"
    grip_horizontal = "\uf3fd"
    grip_vertical = "\uf3fe"
    hammer = "\uf3ff"
    hand_index_fill = "\uf400"
    hand_index_thumb_fill = "\uf401"
    hand_index_thumb = "\uf402"
    hand_index = "\uf403"
    hand_thumbs_down_fill = "\uf404"
    hand_thumbs_down = "\uf405"
    hand_thumbs_up_fill = "\uf406"
    hand_thumbs_up = "\uf407"
    handbag_fill = "\uf408"
    handbag = "\uf409"
    hash = "\uf40a"
    hdd_fill = "\uf40b"
    hdd_network_fill = "\uf40c"
    hdd_network = "\uf40d"
    hdd_rack_fill = "\uf40e"
    hdd_rack = "\uf40f"
    hdd_stack_fill = "\uf410"
    hdd_stack = "\uf411"
    hdd = "\uf412"
    headphones = "\uf413"
    headset = "\uf414"
    heart_fill = "\uf415"
    heart_half = "\uf416"
    heart = "\uf417"
    heptagon_fill = "\uf418"
    heptagon_half = "\uf419"
    heptagon = "\uf41a"
    hexagon_fill = "\uf41b"
    hexagon_half = "\uf41c"
    hexagon = "\uf41d"
    hourglass_bottom = "\uf41e"
    hourglass_split = "\uf41f"
    hourglass_top = "\uf420"
    hourglass = "\uf421"
    house_door_fill = "\uf422"
    house_door = "\uf423"
    house_fill = "\uf424"
    house = "\uf425"
    hr = "\uf426"
    hurricane = "\uf427"
    image_alt = "\uf428"
    image_fill = "\uf429"
    image = "\uf42a"
    images = "\uf42b"
    inbox_fill = "\uf42c"
    inbox = "\uf42d"
    inboxes_fill = "\uf42e"
    inboxes = "\uf42f"
    info_circle_fill = "\uf430"
    info_circle = "\uf431"
    info_square_fill = "\uf432"
    info_square = "\uf433"
    info = "\uf434"
    input_cursor_text = "\uf435"
    input_cursor = "\uf436"
    instagram = "\uf437"
    intersect = "\uf438"
    journal_album = "\uf439"
    journal_arrow_down = "\uf43a"
    journal_arrow_up = "\uf43b"
    journal_bookmark_fill = "\uf43c"
    journal_bookmark = "\uf43d"
    journal_check = "\uf43e"
    journal_code = "\uf43f"
    journal_medical = "\uf440"
    journal_minus = "\uf441"
    journal_plus = "\uf442"
    journal_richtext = "\uf443"
    journal_text = "\uf444"
    journal_x = "\uf445"
    journal = "\uf446"
    journals = "\uf447"
    joystick = "\uf448"
    justify_left = "\uf449"
    justify_right = "\uf44a"
    justify = "\uf44b"
    kanban_fill = "\uf44c"
    kanban = "\uf44d"
    key_fill = "\uf44e"
    key = "\uf44f"
    keyboard_fill = "\uf450"
    keyboard = "\uf451"
    ladder = "\uf452"
    lamp_fill = "\uf453"
    lamp = "\uf454"
    laptop_fill = "\uf455"
    laptop = "\uf456"
    layer_backward = "\uf457"
    layer_forward = "\uf458"
    layers_fill = "\uf459"
    layers_half = "\uf45a"
    layers = "\uf45b"
    layout_sidebar_inset_reverse = "\uf45c"
    layout_sidebar_inset = "\uf45d"
    layout_sidebar_reverse = "\uf45e"
    layout_sidebar = "\uf45f"
    layout_split = "\uf460"
    layout_text_sidebar_reverse = "\uf461"
    layout_text_sidebar = "\uf462"
    layout_text_window_reverse = "\uf463"
    layout_text_window = "\uf464"
    layout_three_columns = "\uf465"
    layout_wtf = "\uf466"
    life_preserver = "\uf467"
    lightbulb_fill = "\uf468"
    lightbulb_off_fill = "\uf469"
    lightbulb_off = "\uf46a"
    lightbulb = "\uf46b"
    lightning_charge_fill = "\uf46c"
    lightning_charge = "\uf46d"
    lightning_fill = "\uf46e"
    lightning = "\uf46f"
    link_45deg = "\uf470"
    link = "\uf471"
    linkedin = "\uf472"
    list_check = "\uf473"
    list_nested = "\uf474"
    list_ol = "\uf475"
    list_stars = "\uf476"
    list_task = "\uf477"
    list_ul = "\uf478"
    list = "\uf479"
    lock_fill = "\uf47a"
    lock = "\uf47b"
    mailbox = "\uf47c"
    mailbox2 = "\uf47d"
    map_fill = "\uf47e"
    map = "\uf47f"
    markdown_fill = "\uf480"
    markdown = "\uf481"
    mask = "\uf482"
    megaphone_fill = "\uf483"
    megaphone = "\uf484"
    menu_app_fill = "\uf485"
    menu_app = "\uf486"
    menu_button_fill = "\uf487"
    menu_button_wide_fill = "\uf488"
    menu_button_wide = "\uf489"
    menu_button = "\uf48a"
    menu_down = "\uf48b"
    menu_up = "\uf48c"
    mic_fill = "\uf48d"
    mic_mute_fill = "\uf48e"
    mic_mute = "\uf48f"
    mic = "\uf490"
    minecart_loaded = "\uf491"
    minecart = "\uf492"
    moisture = "\uf493"
    moon_fill = "\uf494"
    moon_stars_fill = "\uf495"
    moon_stars = "\uf496"
    moon = "\uf497"
    mouse_fill = "\uf498"
    mouse = "\uf499"
    mouse2_fill = "\uf49a"
    mouse2 = "\uf49b"
    mouse3_fill = "\uf49c"
    mouse3 = "\uf49d"
    music_note_beamed = "\uf49e"
    music_note_list = "\uf49f"
    music_note = "\uf4a0"
    music_player_fill = "\uf4a1"
    music_player = "\uf4a2"
    newspaper = "\uf4a3"
    node_minus_fill = "\uf4a4"
    node_minus = "\uf4a5"
    node_plus_fill = "\uf4a6"
    node_plus = "\uf4a7"
    nut_fill = "\uf4a8"
    nut = "\uf4a9"
    octagon_fill = "\uf4aa"
    octagon_half = "\uf4ab"
    octagon = "\uf4ac"
    option = "\uf4ad"
    outlet = "\uf4ae"
    paint_bucket = "\uf4af"
    palette_fill = "\uf4b0"
    palette = "\uf4b1"
    palette2 = "\uf4b2"
    paperclip = "\uf4b3"
    paragraph = "\uf4b4"
    patch_check_fill = "\uf4b5"
    patch_check = "\uf4b6"
    patch_exclamation_fill = "\uf4b7"
    patch_exclamation = "\uf4b8"
    patch_minus_fill = "\uf4b9"
    patch_minus = "\uf4ba"
    patch_plus_fill = "\uf4bb"
    patch_plus = "\uf4bc"
    patch_question_fill = "\uf4bd"
    patch_question = "\uf4be"
    pause_btn_fill = "\uf4bf"
    pause_btn = "\uf4c0"
    pause_circle_fill = "\uf4c1"
    pause_circle = "\uf4c2"
    pause_fill = "\uf4c3"
    pause = "\uf4c4"
    peace_fill = "\uf4c5"
    peace = "\uf4c6"
    pen_fill = "\uf4c7"
    pen = "\uf4c8"
    pencil_fill = "\uf4c9"
    pencil_square = "\uf4ca"
    pencil = "\uf4cb"
    pentagon_fill = "\uf4cc"
    pentagon_half = "\uf4cd"
    pentagon = "\uf4ce"
    people_fill = "\uf4cf"
    people = "\uf4d0"
    percent = "\uf4d1"
    person_badge_fill = "\uf4d2"
    person_badge = "\uf4d3"
    person_bounding_box = "\uf4d4"
    person_check_fill = "\uf4d5"
    person_check = "\uf4d6"
    person_circle = "\uf4d7"
    person_dash_fill = "\uf4d8"
    person_dash = "\uf4d9"
    person_fill = "\uf4da"
    person_lines_fill = "\uf4db"
    person_plus_fill = "\uf4dc"
    person_plus = "\uf4dd"
    person_square = "\uf4de"
    person_x_fill = "\uf4df"
    person_x = "\uf4e0"
    person = "\uf4e1"
    phone_fill = "\uf4e2"
    phone_landscape_fill = "\uf4e3"
    phone_landscape = "\uf4e4"
    phone_vibrate_fill = "\uf4e5"
    phone_vibrate = "\uf4e6"
    phone = "\uf4e7"
    pie_chart_fill = "\uf4e8"
    pie_chart = "\uf4e9"
    pin_angle_fill = "\uf4ea"
    pin_angle = "\uf4eb"
    pin_fill = "\uf4ec"
    pin = "\uf4ed"
    pip_fill = "\uf4ee"
    pip = "\uf4ef"
    play_btn_fill = "\uf4f0"
    play_btn = "\uf4f1"
    play_circle_fill = "\uf4f2"
    play_circle = "\uf4f3"
    play_fill = "\uf4f4"
    play = "\uf4f5"
    plug_fill = "\uf4f6"
    plug = "\uf4f7"
    plus_circle_dotted = "\uf4f8"
    plus_circle_fill = "\uf4f9"
    plus_circle = "\uf4fa"
    plus_square_dotted = "\uf4fb"
    plus_square_fill = "\uf4fc"
    plus_square = "\uf4fd"
    plus = "\uf4fe"
    power = "\uf4ff"
    printer_fill = "\uf500"
    printer = "\uf501"
    puzzle_fill = "\uf502"
    puzzle = "\uf503"
    question_circle_fill = "\uf504"
    question_circle = "\uf505"
    question_diamond_fill = "\uf506"
    question_diamond = "\uf507"
    question_octagon_fill = "\uf508"
    question_octagon = "\uf509"
    question_square_fill = "\uf50a"
    question_square = "\uf50b"
    question = "\uf50c"
    rainbow = "\uf50d"
    receipt_cutoff = "\uf50e"
    receipt = "\uf50f"
    reception_0 = "\uf510"
    reception_1 = "\uf511"
    reception_2 = "\uf512"
    reception_3 = "\uf513"
    reception_4 = "\uf514"
    record_btn_fill = "\uf515"
    record_btn = "\uf516"
    record_circle_fill = "\uf517"
    record_circle = "\uf518"
    record_fill = "\uf519"
    record = "\uf51a"
    record2_fill = "\uf51b"
    record2 = "\uf51c"
    reply_all_fill = "\uf51d"
    reply_all = "\uf51e"
    reply_fill = "\uf51f"
    reply = "\uf520"
    rss_fill = "\uf521"
    rss = "\uf522"
    rulers = "\uf523"
    save_fill = "\uf524"
    save = "\uf525"
    save2_fill = "\uf526"
    save2 = "\uf527"
    scissors = "\uf528"
    screwdriver = "\uf529"
    search = "\uf52a"
    segmented_nav = "\uf52b"
    server = "\uf52c"
    share_fill = "\uf52d"
    share = "\uf52e"
    shield_check = "\uf52f"
    shield_exclamation = "\uf530"
    shield_fill_check = "\uf531"
    shield_fill_exclamation = "\uf532"
    shield_fill_minus = "\uf533"
    shield_fill_plus = "\uf534"
    shield_fill_x = "\uf535"
    shield_fill = "\uf536"
    shield_lock_fill = "\uf537"
    shield_lock = "\uf538"
    shield_minus = "\uf539"
    shield_plus = "\uf53a"
    shield_shaded = "\uf53b"
    shield_slash_fill = "\uf53c"
    shield_slash = "\uf53d"
    shield_x = "\uf53e"
    shield = "\uf53f"
    shift_fill = "\uf540"
    shift = "\uf541"
    shop_window = "\uf542"
    shop = "\uf543"
    shuffle = "\uf544"
    signpost_2_fill = "\uf545"
    signpost_2 = "\uf546"
    signpost_fill = "\uf547"
    signpost_split_fill = "\uf548"
    signpost_split = "\uf549"
    signpost = "\uf54a"
    sim_fill = "\uf54b"
    sim = "\uf54c"
    skip_backward_btn_fill = "\uf54d"
    skip_backward_btn = "\uf54e"
    skip_backward_circle_fill = "\uf54f"
    skip_backward_circle = "\uf550"
    skip_backward_fill = "\uf551"
    skip_backward = "\uf552"
    skip_end_btn_fill = "\uf553"
    skip_end_btn = "\uf554"
    skip_end_circle_fill = "\uf555"
    skip_end_circle = "\uf556"
    skip_end_fill = "\uf557"
    skip_end = "\uf558"
    skip_forward_btn_fill = "\uf559"
    skip_forward_btn = "\uf55a"
    skip_forward_circle_fill = "\uf55b"
    skip_forward_circle = "\uf55c"
    skip_forward_fill = "\uf55d"
    skip_forward = "\uf55e"
    skip_start_btn_fill = "\uf55f"
    skip_start_btn = "\uf560"
    skip_start_circle_fill = "\uf561"
    skip_start_circle = "\uf562"
    skip_start_fill = "\uf563"
    skip_start = "\uf564"
    slack = "\uf565"
    slash_circle_fill = "\uf566"
    slash_circle = "\uf567"
    slash_square_fill = "\uf568"
    slash_square = "\uf569"
    slash = "\uf56a"
    sliders = "\uf56b"
    smartwatch = "\uf56c"
    snow = "\uf56d"
    snow2 = "\uf56e"
    snow3 = "\uf56f"
    sort_alpha_down_alt = "\uf570"
    sort_alpha_down = "\uf571"
    sort_alpha_up_alt = "\uf572"
    sort_alpha_up = "\uf573"
    sort_down_alt = "\uf574"
    sort_down = "\uf575"
    sort_numeric_down_alt = "\uf576"
    sort_numeric_down = "\uf577"
    sort_numeric_up_alt = "\uf578"
    sort_numeric_up = "\uf579"
    sort_up_alt = "\uf57a"
    sort_up = "\uf57b"
    soundwave = "\uf57c"
    speaker_fill = "\uf57d"
    speaker = "\uf57e"
    speedometer = "\uf57f"
    speedometer2 = "\uf580"
    spellcheck = "\uf581"
    square_fill = "\uf582"
    square_half = "\uf583"
    square = "\uf584"
    stack = "\uf585"
    star_fill = "\uf586"
    star_half = "\uf587"
    star = "\uf588"
    stars = "\uf589"
    stickies_fill = "\uf58a"
    stickies = "\uf58b"
    sticky_fill = "\uf58c"
    sticky = "\uf58d"
    stop_btn_fill = "\uf58e"
    stop_btn = "\uf58f"
    stop_circle_fill = "\uf590"
    stop_circle = "\uf591"
    stop_fill = "\uf592"
    stop = "\uf593"
    stoplights_fill = "\uf594"
    stoplights = "\uf595"
    stopwatch_fill = "\uf596"
    stopwatch = "\uf597"
    subtract = "\uf598"
    suit_club_fill = "\uf599"
    suit_club = "\uf59a"
    suit_diamond_fill = "\uf59b"
    suit_diamond = "\uf59c"
    suit_heart_fill = "\uf59d"
    suit_heart = "\uf59e"
    suit_spade_fill = "\uf59f"
    suit_spade = "\uf5a0"
    sun_fill = "\uf5a1"
    sun = "\uf5a2"
    sunglasses = "\uf5a3"
    sunrise_fill = "\uf5a4"
    sunrise = "\uf5a5"
    sunset_fill = "\uf5a6"
    sunset = "\uf5a7"
    symmetry_horizontal = "\uf5a8"
    symmetry_vertical = "\uf5a9"
    table = "\uf5aa"
    tablet_fill = "\uf5ab"
    tablet_landscape_fill = "\uf5ac"
    tablet_landscape = "\uf5ad"
    tablet = "\uf5ae"
    tag_fill = "\uf5af"
    tag = "\uf5b0"
    tags_fill = "\uf5b1"
    tags = "\uf5b2"
    telegram = "\uf5b3"
    telephone_fill = "\uf5b4"
    telephone_forward_fill = "\uf5b5"
    telephone_forward = "\uf5b6"
    telephone_inbound_fill = "\uf5b7"
    telephone_inbound = "\uf5b8"
    telephone_minus_fill = "\uf5b9"
    telephone_minus = "\uf5ba"
    telephone_outbound_fill = "\uf5bb"
    telephone_outbound = "\uf5bc"
    telephone_plus_fill = "\uf5bd"
    telephone_plus = "\uf5be"
    telephone_x_fill = "\uf5bf"
    telephone_x = "\uf5c0"
    telephone = "\uf5c1"
    terminal_fill = "\uf5c2"
    terminal = "\uf5c3"
    text_center = "\uf5c4"
    text_indent_left = "\uf5c5"
    text_indent_right = "\uf5c6"
    text_left = "\uf5c7"
    text_paragraph = "\uf5c8"
    text_right = "\uf5c9"
    textarea_resize = "\uf5ca"
    textarea_t = "\uf5cb"
    textarea = "\uf5cc"
    thermometer_half = "\uf5cd"
    thermometer_high = "\uf5ce"
    thermometer_low = "\uf5cf"
    thermometer_snow = "\uf5d0"
    thermometer_sun = "\uf5d1"
    thermometer = "\uf5d2"
    three_dots_vertical = "\uf5d3"
    three_dots = "\uf5d4"
    toggle_off = "\uf5d5"
    toggle_on = "\uf5d6"
    toggle2_off = "\uf5d7"
    toggle2_on = "\uf5d8"
    toggles = "\uf5d9"
    toggles2 = "\uf5da"
    tools = "\uf5db"
    tornado = "\uf5dc"
    trash_fill = "\uf5dd"
    trash = "\uf5de"
    trash2_fill = "\uf5df"
    trash2 = "\uf5e0"
    tree_fill = "\uf5e1"
    tree = "\uf5e2"
    triangle_fill = "\uf5e3"
    triangle_half = "\uf5e4"
    triangle = "\uf5e5"
    trophy_fill = "\uf5e6"
    trophy = "\uf5e7"
    tropical_storm = "\uf5e8"
    truck_flatbed = "\uf5e9"
    truck = "\uf5ea"
    tsunami = "\uf5eb"
    tv_fill = "\uf5ec"
    tv = "\uf5ed"
    twitch = "\uf5ee"
    twitter = "\uf5ef"
    type_bold = "\uf5f0"
    type_h1 = "\uf5f1"
    type_h2 = "\uf5f2"
    type_h3 = "\uf5f3"
    type_italic = "\uf5f4"
    type_strikethrough = "\uf5f5"
    type_underline = "\uf5f6"
    type = "\uf5f7"
    ui_checks_grid = "\uf5f8"
    ui_checks = "\uf5f9"
    ui_radios_grid = "\uf5fa"
    ui_radios = "\uf5fb"
    umbrella_fill = "\uf5fc"
    umbrella = "\uf5fd"
    union = "\uf5fe"
    unlock_fill = "\uf5ff"
    unlock = "\uf600"
    upc_scan = "\uf601"
    upc = "\uf602"
    upload = "\uf603"
    vector_pen = "\uf604"
    view_list = "\uf605"
    view_stacked = "\uf606"
    vinyl_fill = "\uf607"
    vinyl = "\uf608"
    voicemail = "\uf609"
    volume_down_fill = "\uf60a"
    volume_down = "\uf60b"
    volume_mute_fill = "\uf60c"
    volume_mute = "\uf60d"
    volume_off_fill = "\uf60e"
    volume_off = "\uf60f"
    volume_up_fill = "\uf610"
    volume_up = "\uf611"
    vr = "\uf612"
    wallet_fill = "\uf613"
    wallet = "\uf614"
    wallet2 = "\uf615"
    watch = "\uf616"
    water = "\uf617"
    whatsapp = "\uf618"
    wifi_1 = "\uf619"
    wifi_2 = "\uf61a"
    wifi_off = "\uf61b"
    wifi = "\uf61c"
    wind = "\uf61d"
    window_dock = "\uf61e"
    window_sidebar = "\uf61f"
    window = "\uf620"
    wrench = "\uf621"
    x_circle_fill = "\uf622"
    x_circle = "\uf623"
    x_diamond_fill = "\uf624"
    x_diamond = "\uf625"
    x_octagon_fill = "\uf626"
    x_octagon = "\uf627"
    x_square_fill = "\uf628"
    x_square = "\uf629"
    x = "\uf62a"
    youtube = "\uf62b"
    zoom_in = "\uf62c"
    zoom_out = "\uf62d"
    bank = "\uf62e"
    bank2 = "\uf62f"
    bell_slash_fill = "\uf630"
    bell_slash = "\uf631"
    cash_coin = "\uf632"
    check_lg = "\uf633"
    coin = "\uf634"
    currency_bitcoin = "\uf635"
    currency_dollar = "\uf636"
    currency_euro = "\uf637"
    currency_exchange = "\uf638"
    currency_pound = "\uf639"
    currency_yen = "\uf63a"
    dash_lg = "\uf63b"
    exclamation_lg = "\uf63c"
    file_earmark_pdf_fill = "\uf63d"
    file_earmark_pdf = "\uf63e"
    file_pdf_fill = "\uf63f"
    file_pdf = "\uf640"
    gender_ambiguous = "\uf641"
    gender_female = "\uf642"
    gender_male = "\uf643"
    gender_trans = "\uf644"
    headset_vr = "\uf645"
    info_lg = "\uf646"
    mastodon = "\uf647"
    messenger = "\uf648"
    piggy_bank_fill = "\uf649"
    piggy_bank = "\uf64a"
    pin_map_fill = "\uf64b"
    pin_map = "\uf64c"
    plus_lg = "\uf64d"
    question_lg = "\uf64e"
    recycle = "\uf64f"
    reddit = "\uf650"
    safe_fill = "\uf651"
    safe2_fill = "\uf652"
    safe2 = "\uf653"
    sd_card_fill = "\uf654"
    sd_card = "\uf655"
    skype = "\uf656"
    slash_lg = "\uf657"
    translate = "\uf658"
    x_lg = "\uf659"
    safe = "\uf65a"
