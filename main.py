import os
from nicegui import ui

# Head elements, fonts, icons, Lenis scroll, and custom CSS injection
ui.add_head_html("""
    <!-- Tailwind CSS v4 Browser Compiler -->
    <script src="https://unpkg.com/@tailwindcss/browser@4"></script>
    <style type="text/tailwindcss">
        @theme {
            --font-sans: 'Inter', sans-serif;
            --font-outfit: 'Outfit', sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
            
            /* Define the custom spacing values used in the HTML design */
            --spacing-4_5: 1.125rem;
            --spacing-6_5: 1.625rem;
            --spacing-14: 3.5rem;
        }
    </style>

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    
    <!-- Icon Libraries -->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css">
    
    <!-- Lenis Smooth Scroll -->
    <link rel="stylesheet" href="https://unpkg.com/lenis@1/dist/lenis.css">
    <script src="https://cdn.jsdelivr.net/npm/lenis@1/dist/lenis.min.js"></script>
    
    <!-- GSAP for premium animations -->
    <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/ScrollTrigger.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/TextPlugin.min.js"></script>

    <style>
        body {
            background-color: #020205;
            color: #f4f4f5;
            font-family: 'Inter', sans-serif;
            margin: 0;
            padding: 0;
            overflow-x: hidden;
        }

        /* Override Quasar link and button styles globally */
        a {
            text-decoration: none !important;
            color: inherit;
        }
        a:hover {
            text-decoration: none !important;
        }

        .font-outfit { font-family: 'Outfit', sans-serif; }
        .font-mono { font-family: 'JetBrains Mono', monospace; }

        /* Mouse-tracking Grid Spotlight */
        .cyber-grid-container {
            position: absolute;
        }
        
        .base-grid {
            position: absolute;
            inset: 0;
            background-image: 
                linear-gradient(to right, rgba(255, 255, 255, 0.007) 1px, transparent 1px),
                linear-gradient(to bottom, rgba(255, 255, 255, 0.007) 1px, transparent 1px);
            background-size: 32px 32px;
            pointer-events: none;
            z-index: 1;
        }

        .glow-grid {
            position: absolute;
            inset: 0;
            background-image: 
                linear-gradient(to right, rgba(99, 102, 241, 0.04) 1px, transparent 1px),
                linear-gradient(to bottom, rgba(99, 102, 241, 0.04) 1px, transparent 1px);
            background-size: 32px 32px;
            mask-image: radial-gradient(circle 350px at var(--mouse-x, -9999px) var(--mouse-y, -9999px), black 20%, transparent 100%);
            -webkit-mask-image: radial-gradient(circle 350px at var(--mouse-x, -9999px) var(--mouse-y, -9999px), black 20%, transparent 100%);
            pointer-events: none;
            z-index: 2;
        }

        /* Glow Blobs */
        @keyframes float-slow {
            0%, 100% { transform: translateY(0px) scale(1); }
            50% { transform: translateY(-30px) scale(1.05); }
        }
        .blob-1 { animation: float-slow 16s ease-in-out infinite; }
        .blob-2 { animation: float-slow 20s ease-in-out infinite reverse; }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #020205;
        }
        ::-webkit-scrollbar-thumb {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: rgba(99, 102, 241, 0.3);
        }

        /* Premium Gradient Border Cards */
        .gradient-border-card {
            position: relative;
            background: linear-gradient(135deg, rgba(20, 20, 35, 0.3) 0%, rgba(10, 10, 18, 0.5) 100%);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border-radius: 28px;
            transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
            overflow: hidden;
        }

        .gradient-border-card::before {
            content: '';
            position: absolute;
            inset: 0;
            border-radius: 28px;
            padding: 1.5px;
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.04), rgba(255, 255, 255, 0.01));
            -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            pointer-events: none;
            transition: background 0.5s ease;
            z-index: 10;
        }

        /* Card Spotlight Hover effects */
        .gradient-border-card-sp:hover::before {
            background: linear-gradient(135deg, rgba(155, 81, 224, 0.6), rgba(165, 109, 255, 0.15));
        }
        .gradient-border-card-sp:hover {
            transform: translateY(-6px) scale(1.005);
            box-shadow: 0 25px 50px -12px rgba(155, 81, 224, 0.15), 0 0 30px -5px rgba(155, 81, 224, 0.08);
            background: linear-gradient(135deg, rgba(25, 20, 45, 0.4) 0%, rgba(10, 8, 20, 0.6) 100%);
        }

        .gradient-border-card-sf:hover::before {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.6), rgba(6, 182, 212, 0.15));
        }
        .gradient-border-card-sf:hover {
            transform: translateY(-6px) scale(1.005);
            box-shadow: 0 25px 50px -12px rgba(99, 102, 241, 0.15), 0 0 30px -5px rgba(6, 182, 212, 0.08);
            background: linear-gradient(135deg, rgba(15, 20, 45, 0.4) 0%, rgba(5, 8, 22, 0.6) 100%);
        }

        .gradient-border-card-generic::before {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.01));
        }
        .gradient-border-card-generic:hover::before {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0.03));
        }
        .gradient-border-card-generic:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.5);
            background: rgba(25, 25, 35, 0.4);
        }

        .spotlight-element {
            position: absolute;
            inset: 0;
            background: radial-gradient(circle 120px at var(--x, 0px) var(--y, 0px), rgba(255, 255, 255, 0.04), transparent 80%);
            opacity: 0;
            transition: opacity 0.3s;
            pointer-events: none;
            z-index: 1;
        }
        .gradient-border-card:hover .spotlight-element { opacity: 1; }

        /* Hide initially for entrance animations */
        .hero-animate { opacity: 0; transform: translateY(30px) scale(0.95); }
        .scroll-reveal { opacity: 0; transform: translateY(40px); }
    </style>
    
    <script>
        function initAnimations() {
            if (!document.querySelector('.gradient-border-card')) {
                setTimeout(initAnimations, 100);
                return;
            }
            
            // Initialize Lenis Smooth Scroll
            const lenis = new Lenis({
                autoRaf: true,
            });
            lenis.on('scroll', ScrollTrigger.update);
            gsap.ticker.add((time) => {
                lenis.raf(time * 1000);
            });
            gsap.ticker.lagSmoothing(0);
            
            // Register GSAP ScrollTrigger & TextPlugin
            gsap.registerPlugin(ScrollTrigger, TextPlugin);

            // Hero Entrance
            gsap.to(".hero-animate", {
                opacity: 1,
                y: 0,
                scale: 1,
                duration: 1,
                stagger: 0.15,
                ease: "power4.out"
            });

            // Scroll Reveals
            ScrollTrigger.batch(".scroll-reveal", {
                onEnter: batch => gsap.to(batch, {
                    opacity: 1,
                    y: 0,
                    duration: 0.8,
                    stagger: 0.1,
                    ease: "power3.out",
                    overwrite: true
                }),
                start: "top 85%"
            });

            // Magnetic Navigation Buttons
            document.querySelectorAll('.magnetic-btn').forEach(btn => {
                btn.addEventListener('mousemove', (e) => {
                    const rect = btn.getBoundingClientRect();
                    const x = e.clientX - rect.left - rect.width / 2;
                    const y = e.clientY - rect.top - rect.height / 2;
                    gsap.to(btn, {
                        x: x * 0.3,
                        y: y * 0.3,
                        duration: 0.3,
                        ease: "power2.out"
                    });
                });
                btn.addEventListener('mouseleave', () => {
                    gsap.to(btn, { x: 0, y: 0, duration: 0.5, ease: "elastic.out(1, 0.3)" });
                });
            });

            // Card Hover Effects
            document.querySelectorAll('.hover-card').forEach(card => {
                card.addEventListener('mouseenter', () => {
                    gsap.to(card, { 
                        y: -10, 
                        backgroundColor: "rgba(30, 30, 50, 0.4)",
                        borderColor: "rgba(255, 255, 255, 0.2)",
                        duration: 0.4, 
                        ease: "power2.out" 
                    });
                });
                card.addEventListener('mouseleave', () => {
                    gsap.to(card, { 
                        y: 0, 
                        backgroundColor: "rgba(20, 20, 35, 0.3)",
                        borderColor: "transparent",
                        duration: 0.4, 
                        ease: "power2.out" 
                    });
                });
            });

            // Mouse Tracking for Global Grid
            document.addEventListener('mousemove', (e) => {
                document.body.style.setProperty('--mouse-x', `${e.clientX}px`);
                document.body.style.setProperty('--mouse-y', `${e.clientY}px`);
            });

            // Spotlight in Cards
            document.querySelectorAll('.gradient-border-card').forEach(card => {
                card.addEventListener('mousemove', (e) => {
                    const rect = card.getBoundingClientRect();
                    card.style.setProperty('--x', `${e.clientX - rect.left}px`);
                    card.style.setProperty('--y', `${e.clientY - rect.top}px`);
                });
            });
        }
        initAnimations();
    </script>
""", shared=True)

# ── Reusable Component Helpers ───────────────────────────────────────────────

def build_launcher_card(title: str, tag: str, desc: str, bullets: list, btn_text: str, url: str, accent_color: str, card_hover_class: str, icon_svg: str):
    """Generates a premium application launcher card in Python matching index.html."""
    if title == "ScriptPulse":
        bg_class = "bg-[#9B51E0]/10"
        border_class = "border-[#9B51E0]/25"
        text_class = "text-[#A56DFF]"
        bullet_bg = "bg-[#9B51E0]"
    else:
        bg_class = "bg-indigo-500/10"
        border_class = "border-indigo-500/25"
        text_class = "text-indigo-400"
        bullet_bg = "bg-indigo-400"

    with ui.element('div').classes(f'gradient-border-card {card_hover_class} p-8 gap-6 flex flex-col justify-between h-[390px] cursor-pointer') \
            .on('click', lambda: ui.navigate.to(url, new_tab=True)):
        ui.element('div').classes('spotlight-element')
        with ui.element('div').classes('flex flex-col gap-4 relative z-20'):
            with ui.element('div').classes('w-full flex justify-between items-center'):
                with ui.element('div').classes('flex items-center gap-3'):
                    with ui.element('div').classes(f'p-2.5 rounded-2xl {bg_class} border {border_class} flex items-center justify-center {text_class}'):
                        ui.html(icon_svg)
                    with ui.element('span').classes('text-2xl font-extrabold text-white font-outfit'): ui.html(title)
                with ui.element('span').classes(f'text-[9px] font-bold {text_class} {bg_class} px-2.5 py-1 border {border_class} rounded-full font-outfit tracking-wider'): ui.html(tag)
            
            with ui.element('p').classes('text-xs md:text-sm text-[#A3A0B3] leading-relaxed mt-2 font-light'): ui.html(desc)
            
            with ui.element('ul').classes('flex flex-wrap gap-2 text-[10px] font-mono text-neutral-400 mt-2'):
                for bullet in bullets:
                    with ui.element('li').classes('bg-white/5 border border-white/5 px-2 py-0.5 rounded-md flex items-center gap-1'):
                        ui.element('span').classes(f'w-1.5 h-1.5 rounded-full {bullet_bg}')
                        with ui.element('span'): ui.html(bullet)
                        
        with ui.element('div').classes('w-full flex justify-between items-center border-t border-white/5 pt-4 relative z-20'):
            with ui.element('span').classes(f'text-xs font-bold {text_class} font-outfit'): ui.html(btn_text)
            with ui.element('span').classes(f'material-icons {text_class} text-sm animate-pulse'): ui.html('open_in_new')

def build_pipeline_card(step_num: str, title: str, desc: str, text_color: str):
    """Generates a pipeline step card in Python."""
    num_color = f"text-[{text_color}]" if text_color.startswith('#') else f"text-{text_color}"
    with ui.element('div').classes('gradient-border-card gradient-border-card-generic p-6 flex flex-col gap-4 transition-all duration-300 scroll-reveal'):
        with ui.element('div').classes('flex items-center justify-between'):
            with ui.element('span').classes(f'text-4xl font-black {num_color} font-outfit'): ui.html(step_num)
            icon_map = {'01': 'analytics', '02': 'dataset', '03': 'videocam'}
            with ui.element('span').classes('material-icons text-neutral-600 text-base'): ui.html(icon_map.get(step_num, 'circle'))
        with ui.element('h4').classes('text-base font-extrabold text-white font-outfit'): ui.html(title)
        with ui.element('p').classes('text-xs text-[#A3A0B3] leading-relaxed font-light'): ui.html(desc)

def build_feature_card(icon_name: str, title: str, desc: str):
    """Generates a system feature card in Python."""
    with ui.element('div').classes('gradient-border-card gradient-border-card-generic p-6.5 gap-4.5 flex items-start transition-all duration-300 scroll-reveal'):
        with ui.element('div').classes('p-2.5 rounded-xl bg-indigo-500/10 border border-indigo-500/25 flex items-center justify-center text-indigo-400 flex-shrink-0'):
            with ui.element('span').classes('material-icons text-base'): ui.html(icon_name)
        with ui.element('div').classes('flex flex-col gap-1.5 grow'):
            with ui.element('h4').classes('text-base font-bold text-white font-outfit'): ui.html(title)
            with ui.element('p').classes('text-xs text-[#A3A0B3] leading-relaxed font-light'): ui.html(desc)

# ── NiceGUI Main Page Route ──────────────────────────────────────────────────

@ui.page('/')
def index():
    # Remove default padding to make it a fullscreen cinematic landing page
    ui.query('.nicegui-content').classes('relative overflow-x-hidden p-0 m-0 gap-0 w-full min-h-screen bg-[#020205] text-[#f4f4f5]')

    # 1. Full viewport background grids and glowing blobs
    with ui.element('div').classes('cyber-grid-container absolute inset-0 w-full min-h-screen pointer-events-none z-0 overflow-hidden'):
        ui.element('div').classes('base-grid')
        ui.element('div').classes('glow-grid')
    
    ui.element('div').classes('absolute w-[800px] h-[800px] rounded-full blur-[180px] pointer-events-none bg-indigo-600/10 -left-[300px] -top-[200px] blob-1 z-0')
    ui.element('div').classes('absolute w-[800px] h-[800px] rounded-full blur-[180px] pointer-events-none bg-rose-500/5 -right-[300px] top-[400px] blob-2 z-0')

    # Main content wrapper (guarantees z-indexing above background layers)
    with ui.element('div').classes('relative z-10 w-full flex flex-col items-center'):
        
        # 2. Sticky Header Navigation
        with ui.element('header').classes('w-full sticky top-0 backdrop-blur-xl bg-[#020205]/75 border-b border-white/5 py-4 px-6 z-50 flex justify-center'):
            with ui.element('div').classes('w-full max-w-[1200px] flex justify-between items-center'):
                # Logo
                with ui.element('div').classes('flex items-center gap-2.5 cursor-pointer').on('click', lambda: ui.run_javascript("window.scrollTo({top: 0, behavior: 'smooth'})")):
                    ui.element('span').classes('ti ti-auto-stories text-indigo-400 text-3xl')
                    with ui.element('div').classes('flex flex-col'):
                        with ui.element('span').classes('text-base font-black font-outfit text-white tracking-widest leading-none'): ui.html('SCRIPTWORKS')
                        with ui.element('span').classes('text-[9px] font-bold text-indigo-400 font-outfit tracking-widest mt-0.5 uppercase'): ui.html('Creative Suite')
                
                # Navigation Link list
                with ui.element('nav').classes('flex items-center gap-8 text-sm font-semibold text-neutral-400 font-outfit'):
                    ui.link('Pipeline', '#pipeline').classes('text-neutral-400 hover:text-white no-underline transition duration-200')
                    ui.link('Features', '#features').classes('text-neutral-400 hover:text-white no-underline transition duration-200')
                    ui.link('Launch ScriptPulse', 'https://scriptpulse-app.streamlit.app', new_tab=True) \
                        .classes('bg-gradient-to-r from-[#9B51E0] to-[#A56DFF] text-white px-5 py-2 rounded-xl shadow-[0_0_20px_rgba(155,81,224,0.25)] hover:scale-[1.03] transition-all duration-300 no-underline')
                    ui.link('Launch SceneForge', 'https://sceneforge-aqua-ocean.reflex.run', new_tab=True) \
                        .classes('bg-gradient-to-r from-indigo-600 to-indigo-500 text-white px-5 py-2 rounded-xl shadow-[0_0_20px_rgba(99,102,241,0.25)] hover:scale-[1.03] transition-all duration-300 no-underline')

        # 3. Hero Section
        with ui.element('section').classes('w-full max-w-[1000px] flex flex-col items-center text-center gap-6 py-20 md:py-32 px-6'):
            with ui.element('span').classes('hero-animate text-[10px] font-extrabold text-indigo-400 bg-indigo-500/10 px-4 py-1.5 border border-indigo-500/30 rounded-full font-outfit tracking-widest uppercase'): ui.html('Integrated Narrative Core')
            with ui.element('h1').classes('hero-animate text-6xl md:text-8xl font-black text-white tracking-tighter font-outfit leading-none mt-2'):
                ui.html('From Script <br class="hidden sm:inline">to Screen.')
            with ui.element('h2').classes('hero-animate text-5xl md:text-7xl font-black text-transparent bg-clip-text bg-gradient-to-r from-[#ff5b99] via-[#ff7e40] to-[#ffbe1a] tracking-tight font-outfit leading-none mt-2'): ui.html('Seamlessly.')
            with ui.element('p').classes('hero-animate text-base md:text-lg text-[#A3A0B3] max-w-[700px] mt-6 leading-relaxed font-light'):
                ui.html('Unifying story analytics with grounded spatial production archives. Run automated pacing checks with <span class="text-white font-medium">ScriptPulse</span>, and resolve world-building discrepancies with <span class="text-white font-medium">SceneForge</span>.')

        # 4. Interactive Showcase Dashboard (Stateful Panel)
        with ui.element('section').classes('w-full max-w-[1200px] px-6 mb-24 relative'):
            with ui.element('div').classes('scroll-reveal w-full gradient-border-card p-1 shadow-[0_30px_80px_rgba(0,0,0,0.8)]'):
                
                # Mac Window Header controls and Tabs Selector
                with ui.element('div').classes('flex items-center justify-between border-b border-white/5 bg-[#08080f]/90 px-5 py-4 rounded-t-[26px]'):
                    with ui.element('div').classes('flex items-center gap-2'):
                        ui.element('span').classes('w-3 h-3 rounded-full bg-[#FF5F56] inline-block')
                        ui.element('span').classes('w-3 h-3 rounded-full bg-[#FFBD2E] inline-block')
                        ui.element('span').classes('w-3 h-3 rounded-full bg-[#27C93F] inline-block')
                    
                    # Stateful Tab Selectors in Python (plain HTML tags)
                    with ui.element('div').classes('flex items-center bg-white/[0.03] border border-white/5 p-1 rounded-xl') as tab_row:
                        sp_btn = ui.element('button').classes('tab-btn flex items-center gap-2 text-xs font-semibold px-4 py-2 rounded-lg bg-white/5 text-white transition-all duration-300').props('id="btn-sp"').on('click', lambda: switch_tab('sp'))
                        with sp_btn:
                            with ui.element('span').classes('material-icons text-sm text-[#A56DFF]'): ui.html('analytics')
                            with ui.element('span'): ui.html('ScriptPulse')

                        sf_btn = ui.element('button').classes('tab-btn flex items-center gap-2 text-xs font-semibold px-4 py-2 rounded-lg text-neutral-400 hover:text-white transition-all duration-300').props('id="btn-sf"').on('click', lambda: switch_tab('sf'))
                        with sf_btn:
                            with ui.element('span').classes('material-icons text-sm text-indigo-400'): ui.html('forum')
                            with ui.element('span'): ui.html('SceneForge')
                            
                    with ui.element('div').classes('text-[10px] text-neutral-500 font-mono hidden md:block'): ui.html('status: active')

                # Tabs switching reactive logic combining Python State and GSAP execution
                def switch_tab(tab_id: str):
                    if tab_id == 'sp':
                        sp_btn.classes('bg-white/5 text-white', remove='text-neutral-400')
                        sf_btn.classes('text-neutral-400', remove='bg-white/5 text-white')
                        ui.run_javascript("""
                            const paneSp = document.getElementById('pane-sp');
                            const paneSf = document.getElementById('pane-sf');
                            gsap.to(paneSf, { opacity: 0, scale: 0.95, duration: 0.3, onComplete: () => {
                                paneSf.classList.add('hidden');
                                paneSp.classList.remove('hidden');
                                gsap.fromTo(paneSp, { opacity: 0, scale: 0.95 }, { opacity: 1, scale: 1, duration: 0.3, ease: "power2.out" });
                            }});
                        """)
                    else:
                        sf_btn.classes('bg-white/5 text-white', remove='text-neutral-400')
                        sp_btn.classes('text-neutral-400', remove='bg-white/5 text-white')
                        ui.run_javascript("""
                            const paneSp = document.getElementById('pane-sp');
                            const paneSf = document.getElementById('pane-sf');
                            gsap.to(paneSp, { opacity: 0, scale: 0.95, duration: 0.3, onComplete: () => {
                                paneSp.classList.add('hidden');
                                paneSf.classList.remove('hidden');
                                gsap.fromTo(paneSf, { opacity: 0, scale: 0.95 }, { opacity: 1, scale: 1, duration: 0.3, ease: "power2.out" });
                            }});
                        """)

                # Content Window
                with ui.element('div').classes('bg-[#04040a]/90 p-4 md:p-8 rounded-b-[26px] min-h-[500px] relative overflow-hidden flex flex-col'):
                    
                    # ── Pane 1: ScriptPulse Attentional Flow Map ──
                    pane_sp = ui.element('div').classes('pane w-full grid grid-cols-1 lg:grid-cols-12 gap-8 transition-all duration-500 opacity-100 scale-100').props('id="pane-sp"')
                    with pane_sp:
                        with ui.element('div').classes('lg:col-span-8 flex flex-col gap-4'):
                            with ui.element('div').classes('flex justify-between items-end px-2'):
                                with ui.element('div'):
                                    with ui.element('span').classes('text-xs font-bold text-[#A56DFF] tracking-widest font-outfit uppercase'): ui.html('Attentional Pacing Dynamics')
                                    with ui.element('h4').classes('text-xl font-bold mt-1 text-white'): ui.html('Act II Flow Diagnostics')
                                with ui.element('span').classes('text-[10px] font-mono text-emerald-400 bg-emerald-500/10 border border-emerald-500/25 px-2 py-0.5 rounded-full'): ui.html('SYNC_OK')
                            
                            chart_html = """
                            <div class="w-full bg-[#080812] border border-white/5 rounded-2xl p-4 relative h-[260px] flex items-end">
                                <!-- Grid Lines -->
                                <div class="absolute inset-0 p-4 flex flex-col justify-between pointer-events-none opacity-20">
                                    <div class="border-b border-dashed border-white/20 w-full h-0"></div>
                                    <div class="border-b border-dashed border-white/20 w-full h-0"></div>
                                    <div class="border-b border-dashed border-white/20 w-full h-0"></div>
                                    <div class="border-b border-dashed border-white/20 w-full h-0"></div>
                                </div>
                                
                                <svg class="w-full h-full" viewBox="0 0 800 220" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <defs>
                                        <linearGradient id="chartGrad" x1="0" y1="0" x2="0" y2="1">
                                            <stop offset="0%" stop-color="#9B51E0" stop-opacity="0.25"/>
                                            <stop offset="100%" stop-color="#9B51E0" stop-opacity="0"/>
                                        </linearGradient>
                                        <linearGradient id="chartLineGrad" x1="0" y1="0" x2="1" y2="0">
                                            <stop offset="0%" stop-color="#9B51E0"/>
                                            <stop offset="50%" stop-color="#FF3366"/>
                                            <stop offset="100%" stop-color="#fbbf24"/>
                                        </linearGradient>
                                    </defs>
                                    
                                    <path d="M 50 200 C 150 80, 200 240, 300 120 C 400 30, 450 180, 550 90 C 650 30, 700 130, 750 160 L 750 200 L 50 200 Z" fill="url(#chartGrad)"/>
                                    <!-- Foreground Path -->
                                    <path class="pulse-path" d="M 50 200 C 150 80, 200 240, 300 120 C 400 30, 450 180, 550 90 C 650 30, 700 130, 750 160" stroke="url(#chartLineGrad)" stroke-width="3" stroke-linecap="round" fill="none"/>
                                    
                                    <g class="cursor-pointer group">
                                        <circle cx="400" cy="30" r="6" fill="#FF3366" class="animate-ping" style="animation-duration: 3s;"></circle>
                                        <circle cx="400" cy="30" r="5" fill="#FF3366" stroke="#fff" stroke-width="1.5"></circle>
                                    </g>
                                    <g class="cursor-pointer">
                                        <circle cx="200" cy="200" r="5" fill="#00C853" stroke="#fff" stroke-width="1.5"></circle>
                                    </g>
                                    <g class="cursor-pointer">
                                        <circle cx="550" cy="90" r="5" fill="#9B51E0" stroke="#fff" stroke-width="1.5"></circle>
                                    </g>
                                    
                                    <text x="50" y="215" fill="#4b5563" font-size="9" font-family="monospace">ACT I</text>
                                    <text x="380" y="215" fill="#4b5563" font-size="9" font-family="monospace">ACT II CLIMAX</text>
                                    <text x="700" y="215" fill="#4b5563" font-size="9" font-family="monospace">ACT III</text>
                                </svg>
                                
                                <div class="absolute left-[52%] top-[10%] bg-slate-950/90 border border-pink-500/30 rounded-lg p-2.5 backdrop-blur-md shadow-2xl flex flex-col gap-0.5 select-none transition-transform hover:scale-105 duration-200">
                                    <span class="text-[9px] font-bold text-rose-400 font-outfit uppercase">Wormhole Transit Peak</span>
                                    <span class="text-[11px] text-white font-semibold">Tension Index: 96.8%</span>
                                    <span class="text-[9px] text-[#A3A0B3] font-mono mt-0.5">Scene 45: Endurance Wormhole Entry</span>
                                </div>
                            </div>
                            """
                            ui.html(chart_html).classes('w-full')

                        with ui.element('div').classes('lg:col-span-4 flex flex-col gap-5'):
                            # Diagnostics
                            with ui.element('div').classes('bg-[#080812] border border-white/5 rounded-2xl p-5 flex flex-col gap-4 w-full'):
                                with ui.element('span').classes('text-xs font-bold text-neutral-400 uppercase tracking-wider font-outfit'): ui.html('Attentional Diagnostics')
                                with ui.element('div').classes('grid grid-cols-2 gap-3'):
                                    with ui.element('div').classes('bg-white/[0.02] border border-white/5 p-3 rounded-xl flex flex-col text-center'):
                                        with ui.element('span').classes('text-xs text-neutral-400'): ui.html('Pacing Balance')
                                        with ui.element('span').classes('text-lg font-black text-rose-400 mt-1'): ui.html('78%')
                                    with ui.element('div').classes('bg-white/[0.02] border border-white/5 p-3 rounded-xl flex flex-col text-center'):
                                        with ui.element('span').classes('text-xs text-neutral-400'): ui.html('Attentional Density')
                                        with ui.element('span').classes('text-lg font-black text-purple-400 mt-1'): ui.html('High')
                            
                            # Trim Candidates
                            with ui.element('div').classes('bg-[#080812] border border-white/5 rounded-2xl p-5 flex flex-col gap-3 w-full'):
                                with ui.element('span').classes('text-xs font-bold text-rose-400 uppercase tracking-wider font-outfit'): ui.html('Story Audit: Trim Candidates')
                                with ui.element('div').classes('flex flex-col gap-2.5 max-h-[140px] overflow-y-auto'):
                                    # Scene 12
                                    with ui.element('div').classes('flex items-center justify-between bg-white/[0.01] border border-white/5 px-3 py-2 rounded-xl text-xs hover:bg-white/[0.03] transition'):
                                        with ui.element('div').classes('flex flex-col'):
                                            with ui.element('span').classes('font-bold text-white font-outfit'): ui.html('Scene 12 (Drone Chase)')
                                            with ui.element('span').classes('text-[10px] text-neutral-500 font-mono'): ui.html('Recommend -80 words')
                                        with ui.element('span').classes('material-icons text-amber-500 text-sm'): ui.html('warning')
                                    # Scene 42
                                    with ui.element('div').classes('flex items-center justify-between bg-white/[0.01] border border-white/5 px-3 py-2 rounded-xl text-xs hover:bg-white/[0.03] transition'):
                                        with ui.element('div').classes('flex flex-col'):
                                            with ui.element('span').classes('font-bold text-white font-outfit'): ui.html('Scene 42 (NASA Briefing)')
                                            with ui.element('span').classes('text-[10px] text-neutral-500 font-mono'): ui.html('Recommend cut exposition')
                                        with ui.element('span').classes('material-icons text-rose-500 text-sm'): ui.html('error')

                    # ── Pane 2: SceneForge Chatbot (Initially Hidden) ──
                    pane_sf = ui.element('div').classes('pane w-full grid grid-cols-1 lg:grid-cols-12 gap-8 transition-all duration-500 opacity-0 scale-95 hidden').props('id="pane-sf"')
                    with pane_sf:
                        with ui.element('div').classes('lg:col-span-8 flex flex-col gap-4'):
                            with ui.element('div').classes('flex items-center gap-2 px-2'):
                                ui.element('span').classes('w-2.5 h-2.5 rounded-full bg-emerald-500 inline-block animate-pulse')
                                with ui.element('span').classes('text-xs font-bold text-indigo-400 font-outfit tracking-widest uppercase'): ui.html('Grounded RAG Pipeline Session')
                            
                            with ui.element('div').classes('w-full bg-[#080812] border border-white/5 rounded-2xl p-4 flex flex-col gap-4 min-h-[300px] justify-between'):
                                with ui.element('div').classes('flex flex-col gap-3.5 text-xs'):
                                    # User Message
                                    with ui.element('div').classes('flex gap-3 justify-end'):
                                        with ui.element('div').classes('bg-indigo-600 text-white rounded-2xl rounded-tr-none px-4 py-2.5 max-w-[80%] shadow-lg'): ui.html('Verify the wormhole stability. What does TARS say about the Endurance flight?')
                                    
                                    # AI Message with Citation Popovers
                                    with ui.element('div').classes('flex gap-3'):
                                        with ui.element('div').classes('p-2 h-7 w-7 rounded-lg bg-indigo-500/10 border border-indigo-500/25 flex items-center justify-center text-indigo-400 flex-shrink-0 select-none'):
                                            with ui.element('span').classes('material-icons text-sm'): ui.html('smart_toy')
                                        
                                        ai_msg_html = """
                                        <div class="bg-white/[0.03] border border-white/5 text-neutral-300 rounded-2xl rounded-tl-none px-4 py-2.5 max-w-[85%] leading-relaxed">
                                            TARS reports that the stability of the wormhole near Saturn is 98.4%. He also notes that he has a 10% humor setting, meaning he will make jokes about their demise during the journey
                                            
                                            <!-- Citation Popover -->
                                            <span class="relative group cursor-pointer inline-flex items-center gap-0.5 text-[10px] text-cyan-400 bg-cyan-950/45 border border-cyan-800/40 px-2 py-0.5 rounded ml-1 font-mono leading-none">
                                                [Source: Interstellar_Screenplay.pdf - P.68]
                                                <span class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 w-72 p-3.5 bg-slate-950/98 border border-slate-800 rounded-xl text-[10px] text-neutral-300 opacity-0 pointer-events-none group-hover:opacity-100 group-hover:pointer-events-auto transition-opacity duration-300 backdrop-blur-xl shadow-2xl z-50 leading-relaxed font-sans font-normal">
                                                    <span class="text-cyan-400 font-bold block mb-1">Source Excerpt (Technical Manual)</span>
                                                    "...TARS sits by the console. Cooper checks the wormhole coordinates. 'Is it stable, TARS?' TARS replies, 'Stability is 98.4%, Cooper. And I have a 10% humor setting, meaning I will make jokes about our demise.'..."
                                                </span>
                                            </span>.
                                            Additionally, the gravity anomalies detected in Murph's bedroom were organized like binary code
                                             
                                            <!-- Citation Popover 2 -->
                                            <span class="relative group cursor-pointer inline-flex items-center gap-0.5 text-[10px] text-indigo-400 bg-indigo-950/45 border border-indigo-800/40 px-2 py-0.5 rounded ml-1 font-mono leading-none">
                                                [Source: Interstellar_Screenplay.pdf - P.1]
                                                <span class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 w-72 p-3.5 bg-slate-950/98 border border-slate-800 rounded-xl text-[10px] text-neutral-300 opacity-0 pointer-events-none group-hover:opacity-100 group-hover:pointer-events-auto transition-opacity duration-300 backdrop-blur-xl shadow-2xl z-50 leading-relaxed font-sans font-normal">
                                                    <span class="text-indigo-400 font-bold block mb-1">Source Excerpt (Historical Archive)</span>
                                                    "...Murph, 10, watches dust fall in patterns. Cooper enters, smiling. 'It's a gravitational anomaly, Murph.' She frowns. 'It's a ghost, Dad. It's trying to talk to me.' Cooper checks the dust lanes. They are vertical, organized like binary code."
                                                </span>
                                            </span>.
                                        </div>
                                        """
                                        ui.html(ai_msg_html).classes('flex-grow')
                                
                                # Typing bar mockup
                                with ui.element('div').classes('w-full flex items-center gap-2 border-t border-white/5 pt-3'):
                                    with ui.element('div').classes('bg-white/[0.02] border border-white/5 rounded-xl px-4 py-2 text-[11px] text-neutral-500 grow font-mono select-none'): ui.html('Type command or query references...')
                                    with ui.element('button').classes('h-8 w-8 rounded-xl bg-indigo-600 text-white flex items-center justify-center hover:scale-[1.05] transition select-none'):
                                        with ui.element('span').classes('material-icons text-sm'): ui.html('send')

                        with ui.element('div').classes('lg:col-span-4 flex flex-col gap-5'):
                            # Mem0 Memory List
                            with ui.element('div').classes('bg-[#080812] border border-white/5 rounded-2xl p-5 flex flex-col gap-4 w-full'):
                                with ui.element('div').classes('flex items-center gap-2'):
                                    with ui.element('span').classes('material-icons text-indigo-400 text-sm'): ui.html('memory')
                                    with ui.element('span').classes('text-xs font-bold text-neutral-400 tracking-wider font-outfit uppercase'): ui.html('Mem0 Memory Store')
                                
                                with ui.element('div').classes('flex flex-col gap-2 font-mono text-[10px]'):
                                    with ui.element('div').classes('bg-white/[0.02] border border-white/5 p-2.5 rounded-xl flex items-start gap-2 text-neutral-300'):
                                        ui.element('span').classes('w-1.5 h-1.5 rounded-full bg-cyan-400 mt-1 select-none flex-shrink-0')
                                        with ui.element('span'): ui.html('Wormhole detected near Saturn leading to another galaxy with three potentially habitable planets.')
                                    with ui.element('div').classes('bg-white/[0.02] border border-white/5 p-2.5 rounded-xl flex items-start gap-2 text-neutral-300'):
                                        ui.element('span').classes('w-1.5 h-1.5 rounded-full bg-purple-400 mt-1 select-none flex-shrink-0')
                                        with ui.element('span'): ui.html('TARS humor setting is configured to 10%.')
                                    with ui.element('div').classes('bg-white/[0.02] border border-white/5 p-2.5 rounded-xl flex items-start gap-2 text-neutral-300'):
                                        ui.element('span').classes('w-1.5 h-1.5 rounded-full bg-pink-400 mt-1 select-none flex-shrink-0')
                                        with ui.element('span'): ui.html("Gravitational anomaly in Cooper's house manifests as vertical dust lanes representing binary code.")

        # 5. Application Launchers Grid (ScriptPulse and SceneForge)
        with ui.element('section').classes('w-full max-w-[1200px] gap-8 grid grid-cols-1 md:grid-cols-2 px-6 mt-12'):
            # ScriptPulse Launcher
            build_launcher_card(
                title="ScriptPulse",
                tag="AI STORY INTEL",
                desc="Extract emotional spikes, identify slow pacing subplots, and scan prose density across 7 automated pipeline steps. Set structural baselines to match target film genres.",
                bullets=["7-Agent Agentic Pipeline", "Genre Pacing Calibration", "Character Tension Maps"],
                btn_text="Launch Attentional Diagnostics",
                url="https://scriptpulse-app.streamlit.app",
                accent_color="#9B51E0",
                card_hover_class="gradient-border-card-sp",
                icon_svg='<svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>'
            )
            # SceneForge Launcher
            build_launcher_card(
                title="SceneForge",
                tag="RAG CHATBOT",
                desc="Upload production reference guidelines, query scene specs, and extract spatial configurations with perfect grounding. Integrates character profile facts across prompts.",
                bullets=["Hybrid Vector Similarity", "Cross-session Mem0 Store", "Inline Citations & Tooltips"],
                btn_text="Launch Grounded Research",
                url="https://sceneforge-aqua-ocean.reflex.run",
                accent_color="indigo-400",
                card_hover_class="gradient-border-card-sf",
                icon_svg='<svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" /></svg>'
            )

        # 6. Connected Pipeline Section
        with ui.element('section').classes('w-full max-w-[1200px] mt-28 px-6 flex flex-col items-center').props('id="pipeline"'):
            with ui.element('div').classes('w-full bg-gradient-to-b from-[#0e0f1d]/60 to-[#06060c]/40 border border-[#1e223c]/40 rounded-[36px] p-8 md:p-14 gap-12 flex flex-col relative overflow-hidden shadow-[0_20px_60px_rgba(0,0,0,0.6)]'):
                ui.element('div').classes('absolute w-[300px] h-[300px] rounded-full blur-[100px] pointer-events-none bg-indigo-500/5 -bottom-[10%] -left-[10%] z-0')
                
                with ui.element('div').classes('w-full flex flex-col items-center text-center gap-2 relative z-10'):
                    with ui.element('span').classes('text-[10px] font-extrabold text-rose-500 tracking-widest font-outfit uppercase'): ui.html('The Pre-Production Pipeline')
                    with ui.element('h3').classes('text-3xl md:text-5xl font-black text-white font-outfit tracking-tight'): ui.html('Unified Script-to-Stage Workflow')
                    with ui.element('p').classes('text-xs md:text-sm text-[#A3A0B3] max-w-[600px] mt-1.5 leading-relaxed font-light'): ui.html('ScriptWorks Suite bridges creative concepts and staging physics. Streamline pre-production in three continuous phases.')
                
                with ui.element('div').classes('w-full gap-8 grid grid-cols-1 md:grid-cols-3 mt-4 relative z-10'):
                    build_pipeline_card("01", "Narrative Profiling", "Run screenplay drafts through ScriptPulse to catalog characters, tag primary sets, and audit pacing spikes before drafting shot specs.", "rose-500")
                    build_pipeline_card("02", "Scene Grounding", "Upload scene assets and target parameters to SceneForge. Instantly index manuals, stage history, and character background parameters.", "indigo-400")
                    build_pipeline_card("03", "Staging & Shot Design", "Synchronize verified historical references with virtual camera coordinates, focal directions, and skybox lighting sets for crew exports.", "#FFBE1A")

        # 7. Features Grid Section
        with ui.element('section').classes('w-full max-w-[1200px] gap-12 flex flex-col mt-28 px-6 items-center').props('id="features"'):
            with ui.element('div').classes('w-full flex flex-col items-center text-center gap-2'):
                with ui.element('span').classes('text-[10px] font-extrabold text-indigo-400 tracking-widest font-outfit uppercase'): ui.html('System Synchronization')
                with ui.element('h3').classes('text-3xl md:text-5xl font-black text-white font-outfit tracking-tight'): ui.html('Why Connect Script & Staging?')
            
            with ui.element('div').classes('w-full gap-6 grid grid-cols-1 md:grid-cols-2 mt-4'):
                build_feature_card("grid_view", "Automated Set Sizing", "Parse scene settings (INT. Speakeasy vs EXT. Street) to calibrate scene dimensions, geometry limits, and background presets.")
                build_feature_card("people", "Character Casting Link", "Feed character statistics (dialogue frequency, gender tags, age indicators) into virtual casting panels for speed drafting.")
                build_feature_card("wb_sunny", "Contextual Lighting Setup", "Correlate screen descriptions ('late afternoon', 'rainy night') with primary staging shaders, weather profiles, and ambient filters.")
                build_feature_card("videocam", "Shot-to-Text Mapping", "Bind staging cameras directly with lines of dialogue, generating active storyboards with automated view directions.")

        # 8. Footer Section
        with ui.element('footer').classes('w-full max-w-[1200px] mt-32 py-12 px-6 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-6'):
            with ui.element('span').classes('text-xs text-neutral-500 font-outfit'): ui.html('© 2026 SCRIPTWORKS SUITE. ALL RIGHTS RESERVED.')
            with ui.element('div').classes('flex gap-8 text-xs font-bold text-neutral-400 uppercase tracking-widest'):
                ui.link('Privacy', '#').classes('text-neutral-400 hover:text-white no-underline transition')
                ui.link('Terms', '#').classes('text-neutral-400 hover:text-white no-underline transition')
                ui.link('Status', '#').classes('text-neutral-400 hover:text-white no-underline transition')

# Start the NiceGUI server (uses environment variables for host/port if deploying to cloud)
port = int(os.environ.get("PORT", 8550))
host = os.environ.get("HOST", "0.0.0.0" if os.environ.get("PORT") else "127.0.0.1")
ui.run(port=port, host=host, show=True)
