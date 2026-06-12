import flet as ft


def color_with_opacity(opacity: float, color_str: str) -> str:
    """Convert hex color to #AARRGGBB format with given opacity (0.0 - 1.0)."""
    if color_str.startswith("#"):
        hex_val = color_str.lstrip("#")
        if len(hex_val) == 6:
            alpha = f"{int(opacity * 255):02X}"
            return f"#{alpha}{hex_val}"
        elif len(hex_val) == 8:
            alpha = f"{int(opacity * 255):02X}"
            return f"#{alpha}{hex_val[2:]}"
    return color_str


def main(page: ft.Page):
    # ── Page Setup ──────────────────────────────────────────────────────────
    page.title = "ScriptWorks Suite – From Script to Screen"
    page.bgcolor = "#0A0B10"
    page.padding = 0
    page.spacing = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.fonts = {
        "Outfit": "https://fonts.gstatic.com/s/outfit/v11/08A7L5w7M51y-H-vmn8.ttf",
        "Inter": "https://fonts.gstatic.com/s/inter/v13/UcCO3FwrK3iLTeHuS_fvQtMwCp50KnMw2boKoduKmMEVuLyfAZ9hiJ-Ek-_EeA.woff2",
    }
    page.theme = ft.Theme(font_family="Inter")

    # ── Helpers ─────────────────────────────────────────────────────────────

    def launch(url):
        page.run_task(page.launch_url, url)

    def make_hover_button(text, url, accent_color):
        normal_bg = color_with_opacity(0.12, accent_color)
        hover_bg = accent_color
        btn = ft.Container(
            content=ft.Text(
                text,
                color="white",
                weight=ft.FontWeight.BOLD,
                font_family="Outfit",
                size=14,
            ),
            alignment=ft.Alignment.CENTER,
            height=46,
            bgcolor=normal_bg,
            border=ft.Border.all(1.5, accent_color),
            border_radius=10,
            url=ft.Url(url, target=ft.UrlTarget.BLANK),
            animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
        )

        def on_hover(e):
            btn.bgcolor = hover_bg if e.data == "true" else normal_bg
            btn.update()

        btn.on_hover = on_hover
        return btn

    def make_app_card(title, badge_text, badge_color, description,
                      button_text, button_url, glow_color, icon_name):
        border_normal = "#1E2235"

        normal_shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=color_with_opacity(0.15, "#000000"),
            offset=ft.Offset(0, 4),
        )
        hover_shadow = ft.BoxShadow(
            spread_radius=2,
            blur_radius=30,
            color=color_with_opacity(0.35, glow_color),
            offset=ft.Offset(0, 8),
        )

        card_content = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text(
                                badge_text,
                                size=10,
                                weight=ft.FontWeight.BOLD,
                                color="white",
                                font_family="Outfit",
                            ),
                            bgcolor=badge_color,
                            padding=ft.Padding.symmetric(horizontal=10, vertical=4),
                            border_radius=12,
                        ),
                        ft.Icon(icon_name, size=24, color=glow_color),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Container(height=16),
                ft.Text(title, size=28, font_family="Outfit", weight=ft.FontWeight.BOLD, color="white"),
                ft.Container(height=10),
                ft.Text(description, size=13, color="#94A3B8", font_family="Inter"),
                ft.Container(expand=True),
                make_hover_button(button_text, button_url, glow_color),
            ],
            expand=True,
        )

        card = ft.Container(
            content=card_content,
            bgcolor=color_with_opacity(0.65, "#11121E"),
            border=ft.Border.all(1, border_normal),
            border_radius=18,
            padding=28,
            blur=ft.Blur(15, 15),
            shadow=normal_shadow,
            scale=1.0,
            animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT),
            animate_scale=ft.Animation(300, ft.AnimationCurve.EASE_OUT),
            col={"xs": 12, "md": 6},
            height=340,
        )

        def on_hover(e):
            hovered = e.data == "true"
            card.scale = 1.03 if hovered else 1.0
            card.border = ft.Border.all(
                1.5 if hovered else 1,
                glow_color if hovered else border_normal,
            )
            card.shadow = hover_shadow if hovered else normal_shadow
            card.update()

        card.on_hover = on_hover
        return card

    def make_pipeline_step(num, title, desc):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Text(
                                    num,
                                    size=13,
                                    weight=ft.FontWeight.BOLD,
                                    color="#0A0B10",
                                    font_family="Outfit",
                                ),
                                bgcolor="#4FACFE",
                                width=30,
                                height=30,
                                border_radius=15,
                                alignment=ft.Alignment.CENTER,
                            ),
                            ft.Text(title, size=17, font_family="Outfit", weight=ft.FontWeight.BOLD, color="white"),
                        ],
                        spacing=12,
                    ),
                    ft.Container(height=10),
                    ft.Text(desc, size=13, color="#94A3B8"),
                ],
            ),
            col={"xs": 12, "md": 4},
            padding=15,
        )

    def make_feature_item(title, desc, icon):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Icon(icon, size=22, color="#00F2FE"),
                        bgcolor=color_with_opacity(0.1, "#00F2FE"),
                        padding=12,
                        border_radius=12,
                    ),
                    ft.Container(width=14),
                    ft.Column(
                        controls=[
                            ft.Text(title, size=15, font_family="Outfit", weight=ft.FontWeight.BOLD, color="white"),
                            ft.Text(desc, size=12, color="#94A3B8"),
                        ],
                        expand=True,
                        spacing=4,
                    ),
                ],
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
            col={"xs": 12, "md": 6},
            padding=15,
        )

    def clickable_footer_link(label, url):
        """Wrap footer text in a Container to make it clickable."""
        link = ft.Container(
            content=ft.Text(label, size=12, color="#64748B"),
            url=ft.Url(url, target=ft.UrlTarget.BLANK),
        )
        return link

    # ── Ambient background glows ────────────────────────────────────────────
    bg_glow_1 = ft.Container(
        width=500, height=500, border_radius=250,
        gradient=ft.RadialGradient(
            center=ft.Alignment(0, 0), radius=0.5,
            colors=[color_with_opacity(0.12, "#4FACFE"), color_with_opacity(0.0, "#4FACFE")],
        ),
        left=-200, top=-100,
    )
    bg_glow_2 = ft.Container(
        width=600, height=600, border_radius=300,
        gradient=ft.RadialGradient(
            center=ft.Alignment(0, 0), radius=0.5,
            colors=[color_with_opacity(0.10, "#B92B27"), color_with_opacity(0.0, "#B92B27")],
        ),
        right=-250, top=400,
    )

    # ── Header ──────────────────────────────────────────────────────────────
    def make_nav_item(text, target_key):
        btn = ft.Container(
            content=ft.Text(text, size=11, weight=ft.FontWeight.BOLD, font_family="Outfit", color="#94A3B8"),
            padding=ft.Padding.symmetric(horizontal=12, vertical=6),
            border=ft.Border.all(1, "#1E2235"),
            border_radius=8,
            on_click=lambda e: page.run_task(content_col.scroll_to, scroll_key=target_key, duration=800, curve=ft.AnimationCurve.DECELERATE),
            animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
        )

        def on_hover(e):
            hovered = e.data == "true"
            btn.border = ft.Border.all(1, "#4FACFE" if hovered else "#1E2235")
            btn.content.color = "white" if hovered else "#94A3B8"
            btn.update()

        btn.on_hover = on_hover
        return btn

    header_content = ft.Container(
        content=ft.Row(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.AUTO_STORIES, size=22, color="#4FACFE"),
                        ft.Text("SCRIPTWORKS", size=17, weight=ft.FontWeight.BOLD, font_family="Outfit", color="white"),
                        ft.Text("SUITE", size=17, weight=ft.FontWeight.BOLD, font_family="Outfit", color="#B92B27"),
                    ],
                    spacing=8,
                ),
                ft.Row(
                    controls=[
                        make_nav_item("APPS", "apps"),
                        make_nav_item("PIPELINE", "pipeline"),
                        make_nav_item("SYNC FEATURES", "features"),
                    ],
                    spacing=10,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        width=1400,
    )

    header_nav = ft.Container(
        content=header_content,
        alignment=ft.Alignment.CENTER,
        padding=ft.Padding.symmetric(horizontal=30, vertical=18),
        bgcolor=color_with_opacity(0.75, "#0A0B10"),
        blur=ft.Blur(12, 12),
        border=ft.Border(bottom=ft.BorderSide(1, "#1E2235")),
    )

    # ── Hero ─────────────────────────────────────────────────────────────────
    hero_section = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(
                        "INTEGRATED CREATIVE SUITE",
                        size=11, color="#4FACFE",
                        weight=ft.FontWeight.BOLD, font_family="Outfit",
                    ),
                    padding=ft.Padding.symmetric(horizontal=14, vertical=6),
                    bgcolor=color_with_opacity(0.10, "#4FACFE"),
                    border_radius=20,
                    border=ft.Border.all(1, color_with_opacity(0.25, "#4FACFE")),
                ),
                ft.Container(height=24),
                ft.Text(
                    "From Script to Screen.",
                    size=46, font_family="Outfit", color="white",
                    text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.BOLD,
                ),
                ft.Text(
                    "Seamlessly.",
                    size=46, font_family="Outfit", color="#B92B27",
                    text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.BOLD,
                ),
                ft.Container(height=16),
                ft.Container(
                    content=ft.Text(
                        "Connecting narrative structure with spatial pre-visualization. "
                        "Analyze screenplay mechanics with ScriptPulse, and seamlessly "
                        "compose scenes in 3D using SceneForge.",
                        size=15, color="#94A3B8", text_align=ft.TextAlign.CENTER,
                    ),
                    width=720,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.Padding.symmetric(vertical=40),
    )

    # ── App Cards ────────────────────────────────────────────────────────────
    cards_row = ft.ResponsiveRow(
        key="apps",
        controls=[
            make_app_card(
                title="ScriptPulse",
                badge_text="NARRATIVE ANALYSIS",
                badge_color="#1E3A8A",
                description="Harness advanced AI analytics to dissect screenplay structure, evaluate dialogues, identify pacing bottlenecks, and monitor character development timelines.",
                button_text="Launch ScriptPulse",
                button_url="https://scriptpulse-app.streamlit.app",
                glow_color="#00F2FE",
                icon_name=ft.Icons.ANALYTICS_OUTLINED,
            ),
            make_app_card(
                title="SceneForge",
                badge_text="3D STAGING & VISUALIZATION",
                badge_color="#5B21B6",
                description="Instantly convert script scenes into fully interactive 3D spaces. Place virtual cameras, position actors, arrange lighting, and build the physical layout of your story.",
                button_text="Launch SceneForge",
                button_url="https://sceneforge-aqua-ocean.reflex.run",
                glow_color="#D946EF",
                icon_name=ft.Icons.VIEW_IN_AR_OUTLINED,
            ),
        ],
        spacing=30,
    )

    # ── Pipeline Section ─────────────────────────────────────────────────────
    pipeline_section = ft.Container(
        key="pipeline",
        content=ft.Column(
            controls=[
                ft.Text("THE PIPELINE", size=11, weight=ft.FontWeight.BOLD, color="#B92B27", font_family="Outfit"),
                ft.Container(height=8),
                ft.Text("Unified Script-to-Stage Workflow", size=30, font_family="Outfit", weight=ft.FontWeight.BOLD, color="white", text_align=ft.TextAlign.CENTER),
                ft.Container(height=12),
                ft.Container(
                    content=ft.Text(
                        "ScriptWorks Suite links pre-production stages together. No manual translation — just a fluid creative pipeline.",
                        size=14, color="#94A3B8", text_align=ft.TextAlign.CENTER,
                    ),
                    width=620,
                ),
                ft.Container(height=40),
                ft.ResponsiveRow(
                    controls=[
                        make_pipeline_step("01", "Narrative Profiling", "Run script files through ScriptPulse to analyze tone, generate character breakdowns, and tag production locations."),
                        make_pipeline_step("02", "Scene Composition", "Upload script metadata to instantiate 3D scenes in SceneForge, automatically matching sets and staging properties."),
                        make_pipeline_step("03", "Shot Design", "Frame layouts, storyboard camera paths, animate character movements, and export sequence specs to production crews."),
                    ],
                    spacing=20,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor="#0F101A",
        border=ft.Border.all(1, "#1E2235"),
        border_radius=24,
        padding=40,
        margin=ft.Margin.symmetric(vertical=40),
    )

    # ── Features Grid ────────────────────────────────────────────────────────
    features_section = ft.Container(
        key="features",
        content=ft.Column(
            controls=[
                ft.Text("SYSTEM SYNCHRONIZATION", size=11, weight=ft.FontWeight.BOLD, color="#4FACFE", font_family="Outfit"),
                ft.Container(height=8),
                ft.Text("Why Connect Script & Staging?", size=30, font_family="Outfit", weight=ft.FontWeight.BOLD, color="white", text_align=ft.TextAlign.CENTER),
                ft.Container(height=40),
                ft.ResponsiveRow(
                    controls=[
                        make_feature_item("Automated Set Sizing", "Parse descriptive scenes automatically to determine set scale, indoor/outdoor styles, and structural geometry.", ft.Icons.GRID_VIEW_ROUNDED),
                        make_feature_item("Character Casting Link", "Sync character sheets mapping attributes, dialogue frequency, and character pairs directly into 3D templates.", ft.Icons.PEOPLE_ALT_OUTLINED),
                        make_feature_item("Contextual Lighting Setup", "Scene time-of-day and weather profiles are matched with skybox shaders, sun coordinates, and ambient moods.", ft.Icons.LIGHT_MODE_ROUNDED),
                        make_feature_item("Shot-to-Text Mapping", "Associate virtual camera positions, focal lengths, and camera directions directly to specific script lines.", ft.Icons.VIDEOCAM_ROUNDED),
                    ],
                    spacing=30,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.Padding.symmetric(vertical=40),
    )

    # ── Footer ───────────────────────────────────────────────────────────────
    footer = ft.Container(
        content=ft.Column(
            controls=[
                ft.Divider(height=1, color="#1E2235"),
                ft.Container(height=30),
                ft.Row(
                    controls=[
                        ft.Text("© 2026 ScriptWorks Suite. All rights reserved.", size=12, color="#64748B"),
                        ft.Row(
                            controls=[
                                clickable_footer_link("ScriptPulse", "https://scriptpulse-app.streamlit.app"),
                                ft.Text("•", size=12, color="#64748B"),
                                clickable_footer_link("SceneForge", "https://sceneforge-aqua-ocean.reflex.run"),
                            ],
                            spacing=10,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Container(height=30),
            ],
        ),
        padding=ft.Padding.symmetric(horizontal=10),
    )

    # ── Main Layout ──────────────────────────────────────────────────────────
    main_content_container = ft.Container(
        content=ft.Column(
            controls=[
                hero_section,
                cards_row,
                pipeline_section,
                features_section,
                footer,
            ],
            spacing=0,
        ),
        padding=ft.Padding.symmetric(horizontal=20),
        width=1400,
        alignment=ft.Alignment.TOP_CENTER,
        opacity=0.0,
        animate_opacity=ft.Animation(800, ft.AnimationCurve.EASE_OUT),
    )

    content_col = ft.Column(
        controls=[main_content_container],
        scroll=ft.ScrollMode.AUTO,
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    main_stack = ft.Stack(
        controls=[
            bg_glow_1,
            bg_glow_2,
            ft.Column(
                controls=[header_nav, content_col],
                left=0,
                right=0,
                top=0,
                bottom=0,
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            ),
        ],
        expand=True,
    )

    page.add(main_stack)

    # ── Responsiveness & Auto-sizing ─────────────────────────────────────────
    def adjust_size(e):
        target_width = min(1200, page.width - 40)
        main_content_container.width = target_width
        header_content.width = target_width
        main_content_container.update()
        header_content.update()

    page.on_resize = adjust_size
    adjust_size(None)

    # ── Entrance Animation ───────────────────────────────────────────────────
    async def animate_entrance():
        import asyncio
        await asyncio.sleep(0.1)
        main_content_container.opacity = 1.0
        main_content_container.update()

    page.run_task(animate_entrance)


if __name__ == "__main__":
    ft.run(main, port=8550, host="127.0.0.1", view=ft.AppView.WEB_BROWSER)
