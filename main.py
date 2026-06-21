import os
from nicegui import ui

# Head elements, fonts, icons, and custom CSS injection
ui.add_head_html("""
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    
    <!-- Icon Libraries -->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css">
    
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

        .font-outfit { font-family: 'Outfit', sans-serif; }
        .font-mono { font-family: 'JetBrains Mono', monospace; }

        /* Mouse-tracking Grid Spotlight */
        .cyber-grid-container {
            position: relative;
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
        @keyframes float-reverse {
            0%, 100% { transform: translateY(0px) scale(1.05); }
            50% { transform: translateY(30px) scale(1); }
        }
        .blob-1 { animation: float-slow 16s ease-in-out infinite; }
        .blob-2 { animation: float-reverse 20s ease-in-out infinite; }

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
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            pointer-events: none;
            transition: background 0.5s ease;
            z-index: 10;
        }

        /* Card Spotlight Hover effects */
        .gradient-border-card-sp:hover::before {
            background: linear-gradient(135deg, rgba(167, 78, 198, 0.6), rgba(236, 72, 153, 0.15));
        }
        .gradient-border-card-sp:hover {
            transform: translateY(-6px) scale(1.005);
            box-shadow: 0 25px 50px -12px rgba(167, 78, 198, 0.15), 0 0 30px -5px rgba(106, 72, 187, 0.08);
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

        /* SVG Line drawing dash offset animation */
        @keyframes draw {
            to { stroke-dashoffset: 0; }
        }
        .pulse-path {
            stroke-dasharray: 1000;
            stroke-dashoffset: 1000;
            animation: draw 3s cubic-bezier(0.4, 0, 0.2, 1) forwards;
        }

        /* Spotlight radial background circle follow JS */
        .spotlight-element {
            position: absolute;
            inset: 0;
            background: radial-gradient(circle 120px at var(--x, 0px) var(--y, 0px), rgba(255, 255, 255, 0.04), transparent 80%);
            opacity: 0;
            transition: opacity 0.3s;
            pointer-events: none;
            z-index: 1;
        }
        .gradient-border-card:hover .spotlight-element {
            opacity: 1;
        }

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
            
            // Register GSAP ScrollTrigger
            gsap.registerPlugin(ScrollTrigger);

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

            // Mouse tracking spotlight follow
            document.addEventListener('mousemove', (e) => {
                const rect = document.body.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                document.body.style.setProperty('--mouse-x', `${x}px`);
                document.body.style.setProperty('--mouse-y', `${y}px`);
            });

            document.querySelectorAll('.gradient-border-card').forEach((card) => {
                card.addEventListener('mousemove', (e) => {
                    const rect = card.getBoundingClientRect();
                    const x = e.clientX - rect.left;
                    const y = e.clientY - rect.top;
                    card.querySelector('.spotlight-element')?.style.setProperty('--x', `${x}px`);
                    card.querySelector('.spotlight-element')?.style.setProperty('--y', `${y}px`);
                });
            });
        }
        initAnimations();
    </script>
""", shared=True)

# ── Reusable Component Helpers ───────────────────────────────────────────────

def build_launcher_card(title: str, tag: str, desc: str, bullets: list, btn_text: str, url: str, accent_color: str, card_hover_class: str, icon_svg: str):
    """Generates a premium application launcher card in Python."""
    with ui.element('div').classes(f'gradient-border-card {card_hover_class} p-8 gap-6 flex flex-col justify-between h-[390px] cursor-pointer') \
            .on('click', lambda: ui.navigate.to(url, new_tab=True)):
        ui.element('div').classes('spotlight-element')
        with ui.column().classes('gap-4 relative z-20 w-full'):
            with ui.row().classes('w-full justify-between items-center'):
                with ui.row().classes('items-center gap-3'):
                    with ui.element('div').classes(f'p-2.5 rounded-2xl bg-{accent_color}/10 border border-{accent_color}/25 flex items-center justify-center text-{accent_color}'):
                        ui.html(icon_svg)
                    ui.label(title).classes('text-2xl font-extrabold text-white font-outfit')
                ui.label(tag).classes(f'text-[9px] font-bold text-{accent_color} bg-{accent_color}/10 px-2.5 py-1 border border-{accent_color}/25 rounded-full font-outfit tracking-wider')
            
            ui.label(desc).classes('text-xs md:text-sm text-[#A3A0B3] leading-relaxed mt-2 font-light')
            
            with ui.row().classes('flex-wrap gap-2 text-[10px] font-mono text-neutral-400 mt-2'):
                for bullet in bullets:
                    with ui.row().classes('bg-white/5 border border-white/5 px-2 py-0.5 rounded-md items-center gap-1'):
                        ui.element('span').classes(f'w-1.5 h-1.5 rounded-full bg-{accent_color}')
                        ui.label(bullet)
                        
        with ui.row().classes(f'w-full justify-between items-center border-t border-white/5 pt-4 relative z-20 text-{accent_color}'):
            ui.label(btn_text).classes('text-xs font-bold font-outfit')
            ui.element('span').classes('material-icons text-sm animate-pulse').content('open_in_new')

def build_pipeline_card(step_num: str, title: str, desc: str, text_color: str):
    """Generates a pipeline step card in Python."""
    with ui.element('div').classes('gradient-border-card gradient-border-card-generic p-6 flex flex-col gap-4 transition-all duration-300 scroll-reveal'):
        with ui.row().classes('w-full justify-between items-center'):
            ui.label(step_num).classes(f'text-4xl font-black text-{text_color} font-outfit')
            icon_map = {'01': 'analytics', '02': 'dataset', '03': 'videocam'}
            ui.element('span').classes('material-icons text-neutral-600 text-base').content(icon_map.get(step_num, 'circle'))
        ui.label(title).classes('text-base font-extrabold text-white font-outfit')
        ui.label(desc).classes('text-xs text-[#A3A0B3] leading-relaxed font-light')

def build_feature_card(icon_name: str, title: str, desc: str):
    """Generates a system feature card in Python."""
    with ui.element('div').classes('gradient-border-card gradient-border-card-generic p-6.5 gap-4.5 flex items-start transition-all duration-300 scroll-reveal'):
        with ui.element('div').classes('p-2.5 rounded-xl bg-indigo-500/10 border border-indigo-500/25 flex items-center justify-center text-indigo-400 flex-shrink-0'):
            ui.element('span').classes('material-icons text-base').content(icon_name)
        with ui.column().classes('gap-1.5 grow'):
            ui.label(title).classes('text-base font-bold text-white font-outfit')
            ui.label(desc).classes('text-xs text-[#A3A0B3] leading-relaxed font-light')

# ── NiceGUI Main Page Route ──────────────────────────────────────────────────

@ui.page('/')
def index():
    # Remove default padding to make it a fullscreen cinematic landing page
    ui.query('.nicegui-content').classes('p-0 m-0 gap-0 w-full min-h-screen bg-[#020205]')

    # 1. Full viewport background grids and glowing blobs
    with ui.element('div').classes('cyber-grid-container absolute inset-0 w-full min-h-screen pointer-events-none z-0 overflow-hidden'):
        ui.element('div').classes('base-grid')
        ui.element('div').classes('glow-grid')
    
    ui.element('div').classes('absolute w-[800px] h-[800px] rounded-full blur-[180px] pointer-events-none bg-gradient-to-tr from-indigo-600/10 via-purple-600/10 to-transparent -left-[300px] -top-[200px] blob-1 z-0')
    ui.element('div').classes('absolute w-[800px] h-[800px] rounded-full blur-[180px] pointer-events-none bg-gradient-to-br from-pink-600/8 via-rose-500/5 to-transparent -right-[300px] top-[400px] blob-2 z-0')
    ui.element('div').classes('absolute w-[600px] h-[600px] rounded-full blur-[150px] pointer-events-none bg-indigo-500/5 left-[20%] top-[900px] blob-1 z-0')

    # Main content wrapper (guarantees z-indexing above background layers)
    with ui.element('div').classes('relative z-10 w-full flex flex-col items-center'):
        
        # 2. Sticky Header Navigation
        with ui.element('header').classes('w-full sticky top-0 backdrop-blur-xl bg-[#020205]/75 border-b border-white/5 py-4 px-6 z-50 flex justify-center transition-all duration-300'):
            with ui.element('div').classes('w-full max-w-[1200px] flex justify-between items-center'):
                # Logo
                with ui.row().classes('items-center gap-2.5 cursor-pointer').on('click', lambda: ui.run_javascript("window.scrollTo({top: 0, behavior: 'smooth'})")):
                    ui.element('span').classes('material-icons text-indigo-400 text-3xl select-none').content('auto_stories')
                    with ui.column().classes('gap-0'):
                        ui.label('SCRIPTWORKS').classes('text-base font-black font-outfit text-white tracking-widest leading-none')
                        ui.label('CREATIVE SUITE').classes('text-[9px] font-bold text-indigo-400 font-outfit tracking-widest mt-0.5')
                
                # Navigation Link list
                with ui.row().classes('items-center gap-8 text-sm font-semibold text-neutral-400 font-outfit'):
                    ui.link('Pipeline', '#pipeline').classes('hover:text-white transition duration-200')
                    ui.link('Features', '#features').classes('hover:text-white transition duration-200')
                    ui.link('Launch ScriptPulse', 'https://scriptpulse-app.streamlit.app', new_tab=True) \
                        .classes('border border-[#a74ec6]/30 hover:border-[#a74ec6]/80 text-[#d946ef] hover:bg-[#a74ec6]/5 px-4.5 py-2 rounded-xl transition-all duration-300')
                    ui.link('Launch SceneForge', 'https://sceneforge-aqua-ocean.reflex.run', new_tab=True) \
                        .classes('bg-gradient-to-r from-indigo-600 to-indigo-500 hover:from-indigo-500 hover:to-purple-500 hover:scale-[1.03] text-white px-5 py-2 rounded-xl transition-all duration-300 shadow-[0_0_20px_rgba(99,102,241,0.25)] hover:shadow-[0_0_25px_rgba(99,102,241,0.45)]')

        # 3. Hero Section
        with ui.element('section').classes('w-full max-w-[1000px] flex flex-col items-center text-center gap-6 py-20 md:py-28 px-6 mt-4'):
            ui.label('INTEGRATED NARRATIVE CORE').classes('hero-animate text-[10px] font-extrabold text-indigo-400 bg-indigo-500/10 px-4 py-1.5 border border-indigo-500/30 rounded-full font-outfit tracking-widest uppercase select-none')
            ui.element('h1').classes('hero-animate text-6xl md:text-8xl font-black text-white tracking-tighter font-outfit leading-none mt-2 select-none').html('From Script <br class="hidden sm:inline">to Screen.')
            ui.element('h2').classes('hero-animate text-5xl md:text-7xl font-black text-transparent bg-clip-text bg-gradient-to-r from-[#ff5b99] via-[#ff7e40] to-[#ffbe1a] tracking-tight font-outfit leading-none mt-2 select-none filter drop-shadow-sm').content('Seamlessly.')
            ui.element('p').classes('hero-animate text-base md:text-lg text-[#A3A0B3] max-w-[700px] mt-6 leading-relaxed font-light').html('Unifying story analytics with grounded spatial production archives. Run automated pacing checks with <span class="text-white font-medium">ScriptPulse</span>, and resolve world-building discrepancies with <span class="text-white font-medium">SceneForge</span>.')

        # 4. Interactive Showcase Dashboard (Stateful Panel)
        with ui.element('section').classes('w-full max-w-[1200px] px-6 mb-16 relative scroll-reveal'):
            with ui.element('div').classes('w-full gradient-border-card gradient-border-card-generic p-1 md:p-1.5 shadow-[0_30px_80px_rgba(0,0,0,0.8)]'):
                
                # Mac Window Header controls and Tabs Selector
                with ui.row().classes('w-full justify-between items-center border-b border-white/5 bg-[#08080f]/90 px-5 py-4 rounded-t-[26px]'):
                    with ui.row().classes('items-center gap-2'):
                        ui.element('span').classes('w-3 h-3 rounded-full bg-[#FF5F56] inline-block')
                        ui.element('span').classes('w-3 h-3 rounded-full bg-[#FFBD2E] inline-block')
                        ui.element('span').classes('w-3 h-3 rounded-full bg-[#27C93F] inline-block')
                    
                    # Stateful Tab Selectors in Python
                    with ui.row().classes('items-center bg-white/[0.03] border border-white/5 p-1 rounded-xl') as tab_row:
                        sp_btn = ui.button(on_click=lambda: switch_tab('sp')) \
                            .props('flat') \
                            .classes('flex items-center gap-2 text-xs font-semibold px-4 py-2 rounded-lg bg-white/5 text-white transition-all duration-300')
                        with sp_btn:
                            ui.element('span').classes('material-icons text-sm text-[#d946ef]').content('analytics')
                            ui.label('ScriptPulse Dashboard')

                        sf_btn = ui.button(on_click=lambda: switch_tab('sf')) \
                            .props('flat') \
                            .classes('flex items-center gap-2 text-xs font-semibold px-4 py-2 rounded-lg text-neutral-400 hover:text-white transition-all duration-300')
                        with sf_btn:
                            ui.element('span').classes('material-icons text-sm text-indigo-400').content('forum')
                            ui.label('SceneForge RAG Workspace')
                            
                    ui.label('status: sandbox_active.env').classes('text-[10px] text-neutral-500 font-mono hidden md:block')

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
                with ui.element('div').classes('bg-[#04040a]/90 p-4 md:p-8 rounded-b-[26px] min-h-[460px] flex items-center justify-center relative overflow-hidden'):
                    
                    # ── Pane 1: ScriptPulse Attentional Flow Map ──
                    pane_sp = ui.element('div').classes('w-full grid grid-cols-1 lg:grid-cols-12 gap-8 transition-opacity duration-500').props('id="pane-sp"')
                    with pane_sp:
                        with ui.column().classes('lg:col-span-8 flex flex-col gap-4'):
                            with ui.row().classes('w-full justify-between items-center px-2'):
                                with ui.column().classes('gap-0.5'):
                                    ui.label('Attentional Pacing Dynamics').classes('text-xs font-bold text-[#d946ef] tracking-widest font-outfit uppercase')
                                    ui.label('Input: Act_II_Draft_V4.txt').classes('text-[11px] text-neutral-400 font-mono')
                                ui.label('frontiers_aligned').classes('text-[10px] font-mono bg-emerald-500/10 text-emerald-400 border border-emerald-500/25 px-2 py-0.5 rounded-full')
                            
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
                                            <stop offset="0%" stop-color="#d946ef" stop-opacity="0.25"/>
                                            <stop offset="100%" stop-color="#d946ef" stop-opacity="0"/>
                                        </linearGradient>
                                        <linearGradient id="chartLineGrad" x1="0" y1="0" x2="1" y2="0">
                                            <stop offset="0%" stop-color="#a74ec6"/>
                                            <stop offset="50%" stop-color="#f43f5e"/>
                                            <stop offset="100%" stop-color="#fbbf24"/>
                                        </linearGradient>
                                    </defs>
                                    
                                    <path d="M 50 200 C 150 80, 200 240, 300 120 C 400 30, 450 180, 550 90 C 650 30, 700 130, 750 160 L 750 200 L 50 200 Z" fill="url(#chartGrad)"/>
                                    <path class="pulse-path" d="M 50 200 C 150 80, 200 240, 300 120 C 400 30, 450 180, 550 90 C 650 30, 700 130, 750 160" stroke="url(#chartLineGrad)" stroke-width="3" stroke-linecap="round"/>
                                    
                                    <g class="cursor-pointer group">
                                        <circle cx="400" cy="30" r="6" fill="#f43f5e" class="animate-ping" style="animation-duration: 3s;"></circle>
                                        <circle cx="400" cy="30" r="5" fill="#f43f5e" stroke="#fff" stroke-width="1.5"></circle>
                                    </g>
                                    <g class="cursor-pointer">
                                        <circle cx="200" cy="200" r="5" fill="#10b981" stroke="#fff" stroke-width="1.5"></circle>
                                    </g>
                                    <g class="cursor-pointer">
                                        <circle cx="550" cy="90" r="5" fill="#a74ec6" stroke="#fff" stroke-width="1.5"></circle>
                                    </g>
                                    
                                    <text x="50" y="215" fill="#4b5563" font-size="9" font-family="monospace">ACT I</text>
                                    <text x="380" y="215" fill="#4b5563" font-size="9" font-family="monospace">ACT II CLIMAX</text>
                                    <text x="700" y="215" fill="#4b5563" font-size="9" font-family="monospace">ACT III</text>
                                </svg>
                                
                                <div class="absolute left-[52%] top-[10%] bg-slate-950/90 border border-pink-500/30 rounded-lg p-2.5 backdrop-blur-md shadow-2xl flex flex-col gap-0.5 select-none transition-transform hover:scale-105 duration-200">
                                    <span class="text-[9px] font-bold text-rose-400 font-outfit uppercase">Midpoint Climax Detect</span>
                                    <span class="text-[11px] text-white font-semibold">Tension Index: 94.2%</span>
                                    <span class="text-[9px] text-[#A3A0B3] font-mono mt-0.5">Scene 19: Vault Breakout</span>
                                </div>
                            </div>
                            """
                            ui.html(chart_html).classes('w-full')

                        with ui.column().classes('lg:col-span-4 flex flex-col gap-5'):
                            # Diagnostics
                            with ui.element('div').classes('bg-[#080812] border border-white/5 rounded-2xl p-5 flex flex-col gap-4 w-full'):
                                ui.label('Attentional Diagnostics').classes('text-xs font-bold text-neutral-400 tracking-wider font-outfit')
                                with ui.row().classes('w-full gap-3 font-outfit'):
                                    with ui.column().classes('bg-white/[0.02] border border-white/5 p-3 rounded-xl flex-1'):
                                        ui.label('Pacing Balance').classes('text-xs text-neutral-400')
                                        ui.label('84%').classes('text-lg font-black text-rose-400 mt-1')
                                    with ui.column().classes('bg-white/[0.02] border border-white/5 p-3 rounded-xl flex-1'):
                                        ui.label('Attentional Density').classes('text-xs text-neutral-400')
                                        ui.label('Optimal').classes('text-lg font-black text-purple-400 mt-1')
                            
                            # Trim Candidates
                            with ui.element('div').classes('bg-[#080812] border border-white/5 rounded-2xl p-5 flex flex-col gap-3 w-full'):
                                ui.label('Story Audit: Trim Candidates').classes('text-xs font-bold text-rose-400 tracking-wider font-outfit uppercase')
                                with ui.column().classes('w-full gap-2.5 max-h-[140px] overflow-y-auto'):
                                    # Scene 14
                                    with ui.row().classes('w-full justify-between items-center bg-white/[0.01] border border-white/5 px-3 py-2 rounded-xl text-xs hover:bg-white/[0.03] transition'):
                                        with ui.column().classes('gap-0'):
                                            ui.label('Scene 14 (Prose Heavy)').classes('font-bold text-white font-outfit')
                                            ui.label('Recommend -120 words').classes('text-[10px] text-neutral-500 font-mono')
                                        ui.element('span').classes('material-icons text-amber-500 text-sm').content('warning')
                                    # Scene 27
                                    with ui.row().classes('w-full justify-between items-center bg-white/[0.01] border border-white/5 px-3 py-2 rounded-xl text-xs hover:bg-white/[0.03] transition'):
                                        with ui.column().classes('gap-0'):
                                            ui.label('Scene 27 (Double Beat)').classes('font-bold text-white font-outfit')
                                            ui.label('Recommend cut redundancy').classes('text-[10px] text-neutral-500 font-mono')
                                        ui.element('span').classes('material-icons text-rose-500 text-sm').content('error')

                    # ── Pane 2: SceneForge Chatbot (Initially Hidden) ──
                    pane_sf = ui.element('div').classes('w-full grid grid-cols-1 lg:grid-cols-12 gap-8 transition-opacity duration-500 hidden').props('id="pane-sf"')
                    with pane_sf:
                        with ui.column().classes('lg:col-span-8 flex flex-col gap-4'):
                            with ui.row().classes('items-center gap-2 px-2'):
                                ui.element('span').classes('w-2.5 h-2.5 rounded-full bg-emerald-500 inline-block animate-pulse')
                                ui.label('Grounded RAG Pipeline Session').classes('text-xs font-bold text-indigo-400 font-outfit tracking-widest uppercase')
                            
                            with ui.column().classes('w-full bg-[#080812] border border-white/5 rounded-2xl p-4 gap-4 min-h-[300px] justify-between'):
                                with ui.column().classes('w-full gap-3.5 text-xs'):
                                    # User Message
                                    with ui.row().classes('w-full justify-end'):
                                        ui.label('Verify scene 8 speakeasy lights. Are amber filaments authentic to 1925?') \
                                            .classes('bg-indigo-600 text-white rounded-2xl rounded-tr-none px-4 py-2.5 max-w-[80%] shadow-lg')
                                    
                                    # AI Message with Citation Popovers
                                    with ui.row().classes('w-full gap-3 items-start'):
                                        with ui.element('div').classes('p-2 h-7 w-7 rounded-lg bg-indigo-500/10 border border-indigo-500/25 flex items-center justify-center text-indigo-400 flex-shrink-0 select-none'):
                                            ui.element('span').classes('material-icons text-sm').content('smart_toy')
                                        
                                        ai_msg_html = """
                                        <div class="bg-white/[0.03] border border-white/5 text-neutral-300 rounded-2xl rounded-tl-none px-4 py-2.5 max-w-[85%] leading-relaxed">
                                            Yes, amber-colored bulbs were authentic. Although neon glass tube setups were introduced in early 1924, they did not reach standard illicit underground lounges until late 1926
                                            
                                            <!-- Citation Popover -->
                                            <span class="relative group cursor-pointer inline-flex items-center gap-0.5 text-[10px] text-cyan-400 bg-cyan-950/45 border border-cyan-800/40 px-2 py-0.5 rounded ml-1 font-mono leading-none">
                                                [Source: Speakeasy Arch - P.14]
                                                <span class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 w-72 p-3.5 bg-slate-950/98 border border-slate-800 rounded-xl text-[10px] text-neutral-300 opacity-0 pointer-events-none group-hover:opacity-100 group-hover:pointer-events-auto transition-opacity duration-300 backdrop-blur-xl shadow-2xl z-50 leading-relaxed font-sans font-normal">
                                                    <span class="text-cyan-400 font-bold block mb-1">Source Excerpt (Historical Archive)</span>
                                                    "...Chicago basement lounges operated under strict dim-out guidelines. Bulbs were tinted amber using lacquer coats to dampen the light output..."
                                                </span>
                                            </span>.
                                            For Act II Scene 8, I suggest swapping the "red neon glow" with "warm carbon filament spotlights" 
                                            
                                            <!-- Citation Popover 2 -->
                                            <span class="relative group cursor-pointer inline-flex items-center gap-0.5 text-[10px] text-indigo-400 bg-indigo-950/45 border border-indigo-800/40 px-2 py-0.5 rounded ml-1 font-mono leading-none">
                                                [Source: Stage Lighting 1924]
                                                <span class="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 w-72 p-3.5 bg-slate-950/98 border border-slate-800 rounded-xl text-[10px] text-neutral-300 opacity-0 pointer-events-none group-hover:opacity-100 group-hover:pointer-events-auto transition-opacity duration-300 backdrop-blur-xl shadow-2xl z-50 leading-relaxed font-sans font-normal">
                                                    <span class="text-indigo-400 font-bold block mb-1">Source Excerpt (Technical Manual)</span>
                                                    "...The carbon-filament spotlight remained the fixture of choice for staging underground cabaret floors during the transition era..."
                                                </span>
                                            </span>.
                                        </div>
                                        """
                                        ui.html(ai_msg_html).classes('flex-grow')
                                
                                # Typing bar mockup
                                with ui.row().classes('w-full items-center gap-2 border-t border-white/5 pt-3'):
                                    ui.label('Type command or query references...').classes('bg-white/[0.02] border border-white/5 rounded-xl px-4 py-2 text-[11px] text-neutral-500 grow font-mono select-none')
                                    with ui.element('button').classes('h-8 w-8 rounded-xl bg-indigo-600 text-white flex items-center justify-center hover:scale-[1.05] transition select-none'):
                                        ui.element('span').classes('material-icons text-sm').content('send')

                        with ui.column().classes('lg:col-span-4 flex flex-col gap-5'):
                            # Mem0 Memory List
                            with ui.element('div').classes('bg-[#080812] border border-white/5 rounded-2xl p-5 flex flex-col gap-4 w-full'):
                                with ui.row().classes('items-center gap-2'):
                                    ui.element('span').classes('material-icons text-indigo-400 text-sm').content('memory')
                                    ui.label('Mem0 Memory Store').classes('text-xs font-bold text-neutral-400 tracking-wider font-outfit uppercase')
                                
                                with ui.column().classes('w-full gap-2 font-mono text-[10px]'):
                                    with ui.row().classes('w-full bg-white/[0.02] border border-white/5 p-2.5 rounded-xl items-start gap-2 text-neutral-300'):
                                        ui.element('span').classes('w-1.5 h-1.5 rounded-full bg-cyan-400 mt-1 select-none flex-shrink-0')
                                        ui.label('Setting verified as basement speakeasy, Chicago, Dec 1925.')
                                    with ui.row().classes('w-full bg-white/[0.02] border border-white/5 p-2.5 rounded-xl items-start gap-2 text-neutral-300'):
                                        ui.element('span').classes('w-1.5 h-1.5 rounded-full bg-purple-400 mt-1 select-none flex-shrink-0')
                                        ui.label('Inspector Miller has a physical facial tic when questioned about bribery.')
                                    with ui.row().classes('w-full bg-white/[0.02] border border-white/5 p-2.5 rounded-xl items-start gap-2 text-neutral-300'):
                                        ui.element('span').classes('w-1.5 h-1.5 rounded-full bg-pink-400 mt-1 select-none flex-shrink-0')
                                        ui.label("The password required at the speakeasy entrance is 'Blue Canary'.")

        # 5. Application Launchers Grid (ScriptPulse and SceneForge)
        with ui.element('section').classes('w-full max-w-[1200px] gap-8 grid grid-cols-1 md:grid-cols-2 px-6 mt-12 scroll-reveal'):
            # ScriptPulse Launcher
            build_launcher_card(
                title="ScriptPulse",
                tag="AI STORY INTEL",
                desc="Extract emotional spikes, identify slow pacing subplots, and scan prose density across 7 automated pipeline steps. Set structural baselines to match target film genres.",
                bullets=["7-Agent Agentic Pipeline", "Genre Pacing Calibration", "Character Tension Maps"],
                btn_text="Launch Attentional Diagnostics",
                url="https://scriptpulse-app.streamlit.app",
                accent_color="#d946ef",
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
                
                with ui.column().classes('w-full items-center text-center gap-2 relative z-10'):
                    ui.label('The Pre-Production Pipeline').classes('text-[10px] font-extrabold text-rose-500 tracking-widest font-outfit uppercase')
                    ui.label('Unified Script-to-Stage Workflow').classes('text-3xl md:text-5xl font-black text-white font-outfit tracking-tight')
                    ui.label('ScriptWorks Suite bridges creative concepts and staging physics. Streamline pre-production in three continuous phases.').classes('text-xs md:text-sm text-[#A3A0B3] max-w-[600px] mt-1.5 leading-relaxed font-light')
                
                with ui.row().classes('w-full gap-8 grid grid-cols-1 md:grid-cols-3 mt-4 relative z-10'):
                    build_pipeline_card("01", "Narrative Profiling", "Run screenplay drafts through ScriptPulse to catalog characters, tag primary sets, and audit pacing spikes before drafting shot specs.", "rose-500")
                    build_pipeline_card("02", "Scene Grounding", "Upload scene assets and target parameters to SceneForge. Instantly index manuals, stage history, and character background parameters.", "indigo-400")
                    build_pipeline_card("03", "Staging & Shot Design", "Synchronize verified historical references with virtual camera coordinates, focal directions, and skybox lighting sets for crew exports.", "#FFBE1A")

        # 7. Features Grid Section
        with ui.element('section').classes('w-full max-w-[1200px] gap-12 flex flex-col mt-28 px-6 items-center').props('id="features"'):
            with ui.column().classes('w-full items-center text-center gap-2'):
                ui.label('System Synchronization').classes('text-[10px] font-extrabold text-indigo-400 tracking-widest font-outfit uppercase')
                ui.label('Why Connect Script & Staging?').classes('text-3xl md:text-5xl font-black text-white font-outfit tracking-tight')
            
            with ui.row().classes('w-full gap-6 grid grid-cols-1 md:grid-cols-2 mt-4'):
                build_feature_card("grid_view", "Automated Set Sizing", "Parse scene settings (INT. Speakeasy vs EXT. Street) to calibrate scene dimensions, geometry limits, and background presets.")
                build_feature_card("people", "Character Casting Link", "Feed character statistics (dialogue frequency, gender tags, age indicators) into virtual casting panels for speed drafting.")
                build_feature_card("wb_sunny", "Contextual Lighting Setup", "Correlate screen descriptions ('late afternoon', 'rainy night') with primary staging shaders, weather profiles, and ambient filters.")
                build_feature_card("videocam", "Shot-to-Text Mapping", "Bind staging cameras directly with lines of dialogue, generating active storyboards with automated view directions.")

        # 8. Footer Section
        with ui.footer().classes('w-full max-w-[1200px] mt-32 px-6 bg-transparent text-[#f4f4f5] border-t border-white/5 flex flex-col gap-0 justify-center items-center'):
            with ui.row().classes('w-full py-8 flex flex-col md:flex-row justify-between items-center gap-4 text-xs text-neutral-500'):
                ui.label('© 2026 ScriptWorks Suite. All rights reserved.').classes('font-outfit')
                with ui.row().classes('items-center gap-4'):
                    ui.link('ScriptPulse', 'https://scriptpulse-app.streamlit.app', new_tab=True).classes('hover:text-white transition')
                    ui.label('•').classes('text-neutral-700')
                    ui.link('SceneForge', 'https://sceneforge-aqua-ocean.reflex.run', new_tab=True).classes('hover:text-white transition')

# Start the local NiceGUI dev server
ui.run(port=8550, host="127.0.0.1", show=False)

