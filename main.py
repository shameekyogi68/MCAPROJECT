import os
from nicegui import ui

# ── Custom CSS Design System & Theme Overrides ───────────────────────────────

ui.add_head_html("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;700&display=swap');
    
    html {
        scroll-behavior: smooth;
    }
    
    body {
        font-family: 'Inter', sans-serif;
        background-color: #030307;
        color: #f4f4f5;
        margin: 0;
        overflow-x: hidden;
        /* Technical cyber grid overlay */
        background-image: radial-gradient(rgba(255, 255, 255, 0.015) 1px, transparent 1px);
        background-size: 32px 32px;
    }
    
    .font-outfit {
        font-family: 'Outfit', sans-serif;
    }
    
    .font-mono {
        font-family: 'JetBrains Mono', monospace;
    }
    
    /* Text Gradients */
    .text-gradient-purple {
        background: linear-gradient(135deg, #6A48BB 0%, #A74EC6 50%, #D92987 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .text-gradient-blue {
        background: linear-gradient(135deg, #55E0FF 0%, #6366f1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .text-gradient-gold {
        background: linear-gradient(135deg, #FBBF24 0%, #F57946 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .text-gradient-rose {
        background: linear-gradient(135deg, #FF5B99 0%, #D92987 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Premium glassmorphic cards */
    .glass-card {
        background: linear-gradient(135deg, rgba(20, 20, 35, 0.4) 0%, rgba(10, 10, 18, 0.6) 100%);
        backdrop-filter: blur(24px) saturate(1.2);
        border: 1px solid rgba(255, 255, 255, 0.03);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4);
        transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    .glass-card-hover-sp:hover {
        transform: translateY(-8px) scale(1.01);
        border-color: rgba(167, 78, 198, 0.3) !important;
        box-shadow: 0 20px 40px rgba(167, 78, 198, 0.12), 0 0 25px rgba(106, 72, 187, 0.08) !important;
    }

    .glass-card-hover-sf:hover {
        transform: translateY(-8px) scale(1.01);
        border-color: rgba(99, 102, 241, 0.3) !important;
        box-shadow: 0 20px 40px rgba(99, 102, 241, 0.12), 0 0 25px rgba(99, 102, 241, 0.08) !important;
    }
    
    .glass-card-hover-generic:hover {
        transform: translateY(-4px);
        border-color: rgba(255, 255, 255, 0.1) !important;
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3) !important;
    }
    
    /* Buttons */
    .q-btn {
        border-radius: 12px !important;
        text-transform: none !important;
        font-weight: 600 !important;
        letter-spacing: 0.01em !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    .q-btn:hover {
        transform: translateY(-2px);
    }
    
    /* Custom scrollbars */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #030307;
    }
    ::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.06);
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(99, 102, 241, 0.25);
    }
    
    /* Animated glowing background blobs */
    @keyframes float-slow {
        0%, 100% { transform: translateY(0px) scale(1); }
        50% { transform: translateY(-20px) scale(1.05); }
    }
    @keyframes float-reverse {
        0%, 100% { transform: translateY(0px) scale(1.05); }
        50% { transform: translateY(20px) scale(1); }
    }
    .blob-1 {
        animation: float-slow 15s ease-in-out infinite;
    }
    .blob-2 {
        animation: float-reverse 15s ease-in-out infinite;
    }
    
    /* Sticky Nav Blur */
    .sticky-header {
        position: sticky;
        top: 0;
        backdrop-filter: blur(16px);
        background: rgba(3, 3, 7, 0.7);
        border-bottom: 1px solid rgba(255, 255, 255, 0.03);
    }
</style>
""", shared=True)

@ui.page('/')
def index():
    # ── Background glowing blobs ─────────────────────────────────────────────
    ui.element('div').classes('absolute w-[700px] h-[700px] rounded-full blur-[200px] pointer-events-none bg-gradient-to-r from-indigo-500/20 to-purple-600/10 left-[-250px] top-[-150px] blob-1 z-0')
    ui.element('div').classes('absolute w-[700px] h-[700px] rounded-full blur-[200px] pointer-events-none bg-gradient-to-r from-rose-500/15 to-amber-600/10 right-[-250px] top-[250px] blob-2 z-0')
    
    # ── Main Content Container ───────────────────────────────────────────────
    with ui.column().classes('w-full items-center p-0 gap-0 relative min-h-screen z-10'):
        
        # 1. Sticky Header Navigation
        with ui.row().classes('w-full sticky-header justify-center py-4 px-6 z-50'):
            with ui.row().classes('w-full max-w-[1200px] justify-between items-center'):
                # Logo
                with ui.row().classes('items-center gap-2 cursor-pointer').on('click', lambda: ui.navigate.to('/')):
                    ui.icon('auto_stories', color='indigo-400', size='md')
                    with ui.column().classes('gap-0'):
                        ui.label('SCRIPTWORKS').classes('text-base font-black font-outfit text-white tracking-widest leading-none')
                        ui.label('CREATIVE SUITE').classes('text-[9px] font-bold text-indigo-400 font-outfit tracking-widest')
                
                # Nav Links
                with ui.row().classes('items-center gap-8 text-sm font-bold text-neutral-400 font-outfit hidden md:flex'):
                    ui.label('Pipeline').classes('cursor-pointer hover:text-white transition').on('click', lambda: ui.run_javascript("document.getElementById('pipeline').scrollIntoView({behavior: 'smooth'})"))
                    ui.label('Features').classes('cursor-pointer hover:text-white transition').on('click', lambda: ui.run_javascript("document.getElementById('features').scrollIntoView({behavior: 'smooth'})"))
                    ui.button('Launch ScriptPulse', on_click=lambda: ui.navigate.to('https://scriptpulse-app.streamlit.app', new_tab=True)).props('outline color="indigo" size="md"').classes('border-[#6A48BB]/40 hover:border-[#6A48BB] text-[#A74EC6]')
                    ui.button('Launch SceneForge', on_click=lambda: ui.navigate.to('https://sceneforge-aqua-ocean.reflex.run', new_tab=True)).props('color="indigo" size="md"').classes('bg-gradient-to-r from-indigo-600 to-purple-600 border-none shadow-[0_0_20px_rgba(99,102,241,0.3)]')
                
        # 2. Hero Section
        with ui.column().classes('w-full max-w-[950px] items-center text-center gap-6 py-24 px-6 mt-4'):
            ui.label('INTEGRATED NARRATIVE CORE').classes('text-[10px] font-bold text-indigo-400 bg-indigo-500/10 px-4 py-1.5 border border-indigo-500/35 rounded-full font-outfit tracking-widest')
            ui.label('From Script to Screen.').classes('text-6xl md:text-7xl lg:text-8xl font-black text-white tracking-tight font-outfit mt-4 leading-none')
            ui.label('Seamlessly.').classes('text-5xl md:text-6xl lg:text-7xl font-black text-transparent bg-clip-text bg-gradient-to-r from-rose-500 to-amber-500 tracking-tight font-outfit leading-none mt-2')
            ui.label('Connecting screenplay pacing with grounded research intelligence. Analyze narrative mechanics with ScriptPulse, and query production archives with SceneForge.').classes('text-base text-[#A3A0B3] max-w-[720px] mt-6 leading-relaxed')
            
        # 3. Application Cards Grid
        with ui.row().classes('w-full max-w-[1200px] gap-8 grid grid-cols-1 md:grid-cols-2 px-6 mt-8'):
            
            # ScriptPulse Card
            with ui.column().classes('glass-card glass-card-hover-sp p-8 rounded-3xl gap-6 flex flex-col justify-between h-[380px] cursor-pointer') \
                .on('click', lambda: ui.navigate.to('https://scriptpulse-app.streamlit.app', new_tab=True)):
                with ui.column().classes('gap-4'):
                    with ui.row().classes('w-full justify-between items-center'):
                        # Icon + Title
                        with ui.row().classes('items-center gap-3'):
                            ui.element('div').classes('p-2.5 rounded-2xl bg-[#A74EC6]/10 border border-[#A74EC6]/25 flex items-center justify-center') \
                                .content(ui.icon('analytics', color='purple-4', size='sm'))
                            ui.label('ScriptPulse').classes('text-2xl font-extrabold text-white font-outfit')
                        ui.label('AI STORY INTEL').classes('text-[9px] font-bold text-[#A74EC6] bg-[#A74EC6]/10 px-2.5 py-1 border border-[#A74EC6]/25 rounded-full font-outfit tracking-wider')
                    ui.label('Analyze screenplay pacing and attentional flow curves using a 7-agent story intelligence pipeline. Calibrate genre pacing baselines, track character dynamics, and audit scene economy for trim candidates.').classes('text-xs md:text-sm text-[#A3A0B3] leading-relaxed mt-2')
                with ui.row().classes('w-full justify-between items-center border-t border-white/5 pt-4'):
                    ui.label('Launch Application').classes('text-xs font-bold text-[#A74EC6] font-outfit')
                    ui.icon('open_in_new', color='purple-4', size='xs')

            # SceneForge Card
            with ui.column().classes('glass-card glass-card-hover-sf p-8 rounded-3xl gap-6 flex flex-col justify-between h-[380px] cursor-pointer') \
                .on('click', lambda: ui.navigate.to('https://sceneforge-aqua-ocean.reflex.run', new_tab=True)):
                with ui.column().classes('gap-4'):
                    with ui.row().classes('w-full justify-between items-center'):
                        # Icon + Title
                        with ui.row().classes('items-center gap-3'):
                            ui.element('div').classes('p-2.5 rounded-2xl bg-indigo-500/10 border border-indigo-500/25 flex items-center justify-center') \
                                .content(ui.icon('forum', color='indigo-4', size='sm'))
                            ui.label('SceneForge').classes('text-2xl font-extrabold text-white font-outfit')
                        ui.label('RAG CHATBOT').classes('text-[9px] font-bold text-indigo-400 bg-indigo-500/10 px-2.5 py-1 border border-indigo-500/25 rounded-full font-outfit tracking-wider')
                    ui.label('Query screenplays, books, and reference PDFs securely with zero hallucinations. Features hybrid vector similarity/keyword search, Mem0 cross-session memory, and grounded inline citations with hoverable source tooltips.').classes('text-xs md:text-sm text-[#A3A0B3] leading-relaxed mt-2')
                with ui.row().classes('w-full justify-between items-center border-t border-white/5 pt-4'):
                    ui.label('Launch Application').classes('text-xs font-bold text-indigo-400 font-outfit')
                    ui.icon('open_in_new', color='indigo-4', size='xs')

        # 4. Pipeline Section
        with ui.column().classes('w-full max-w-[1200px] bg-[#0E0F19]/40 border border-[#1E2235]/40 rounded-[32px] p-8 md:p-12 gap-10 flex flex-col mt-28 px-6 relative overflow-hidden').props('id="pipeline"'):
            with ui.column().classes('w-full items-center text-center gap-2'):
                ui.label('THE PIPELINE').classes('text-[10px] font-bold text-rose-500 font-outfit tracking-widest')
                ui.label('Unified Script-to-Stage Workflow').classes('text-3xl md:text-4xl font-extrabold text-white font-outfit tracking-tight')
                ui.label('ScriptWorks Suite links pre-production stages together. No manual translation — just a fluid creative pipeline.').classes('text-xs md:text-sm text-[#A3A0B3] max-w-[550px] mt-1 leading-relaxed')
            
            with ui.row().classes('w-full gap-6 grid grid-cols-1 md:grid-cols-3 mt-4'):
                # Step 1
                with ui.column().classes('bg-white/1 p-6 rounded-2xl border border-white/5 gap-3 h-full glass-card-hover-generic transition-all duration-300'):
                    ui.label('01').classes('text-3xl font-black text-rose-500 font-outfit')
                    ui.label('Narrative Profiling').classes('text-base font-bold text-white font-outfit')
                    ui.label('Run script files through ScriptPulse to analyze tone, generate character breakdowns, and tag production locations.').classes('text-xs text-[#A3A0B3] leading-relaxed')
                # Step 2
                with ui.column().classes('bg-white/1 p-6 rounded-2xl border border-white/5 gap-3 h-full glass-card-hover-generic transition-all duration-300'):
                    ui.label('02').classes('text-3xl font-black text-indigo-400 font-outfit')
                    ui.label('Scene Composition').classes('text-base font-bold text-white font-outfit')
                    ui.label('Upload script metadata to instantiate 3D scenes in SceneForge, automatically matching sets and staging properties.').classes('text-xs text-[#A3A0B3] leading-relaxed')
                # Step 3
                with ui.column().classes('bg-white/1 p-6 rounded-2xl border border-white/5 gap-3 h-full glass-card-hover-generic transition-all duration-300'):
                    ui.label('03').classes('text-3xl font-black text-[#FBBF24] font-outfit')
                    ui.label('Shot Design').classes('text-base font-bold text-white font-outfit')
                    ui.label('Frame layouts, storyboard camera paths, animate character movements, and export sequence specs to production crews.').classes('text-xs text-[#A3A0B3] leading-relaxed')

        # 5. Features Grid Section
        with ui.column().classes('w-full max-w-[1200px] gap-12 flex flex-col mt-28 px-6 items-center').props('id="features"'):
            with ui.column().classes('w-full items-center text-center gap-2'):
                ui.label('SYSTEM SYNCHRONIZATION').classes('text-[10px] font-bold text-indigo-400 font-outfit tracking-widest')
                ui.label('Why Connect Script & Staging?').classes('text-3xl md:text-4xl font-extrabold text-white font-outfit tracking-tight')
                
            with ui.row().classes('w-full gap-6 grid grid-cols-1 md:grid-cols-2 mt-4'):
                # Feature 1
                with ui.row().classes('bg-white/1 p-6 rounded-2xl border border-white/5 gap-4 items-start glass-card-hover-generic transition-all duration-300'):
                    ui.element('div').classes('p-2 rounded-xl bg-indigo-500/10 border border-indigo-500/25 flex items-center justify-center') \
                        .content(ui.icon('grid_view', color='indigo-400', size='xs'))
                    with ui.column().classes('gap-1 grow'):
                        ui.label('Automated Set Sizing').classes('text-base font-bold text-white font-outfit')
                        ui.label('Parse descriptive scenes automatically to determine set scale, indoor/outdoor styles, and structural geometry.').classes('text-xs text-[#A3A0B3] leading-relaxed')
                # Feature 2
                with ui.row().classes('bg-white/1 p-6 rounded-2xl border border-white/5 gap-4 items-start glass-card-hover-generic transition-all duration-300'):
                    ui.element('div').classes('p-2 rounded-xl bg-indigo-500/10 border border-indigo-500/25 flex items-center justify-center') \
                        .content(ui.icon('people', color='indigo-400', size='xs'))
                    with ui.column().classes('gap-1 grow'):
                        ui.label('Character Casting Link').classes('text-base font-bold text-white font-outfit')
                        ui.label('Sync character sheets mapping attributes, dialogue frequency, and character pairs directly into 3D templates.').classes('text-xs text-[#A3A0B3] leading-relaxed')
                # Feature 3
                with ui.row().classes('bg-white/1 p-6 rounded-2xl border border-white/5 gap-4 items-start glass-card-hover-generic transition-all duration-300'):
                    ui.element('div').classes('p-2 rounded-xl bg-indigo-500/10 border border-indigo-500/25 flex items-center justify-center') \
                        .content(ui.icon('wb_sunny', color='indigo-400', size='xs'))
                    with ui.column().classes('gap-1 grow'):
                        ui.label('Contextual Lighting Setup').classes('text-base font-bold text-white font-outfit')
                        ui.label('Scene time-of-day and weather profiles are matched with skybox shaders, sun coordinates, and ambient moods.').classes('text-xs text-[#A3A0B3] leading-relaxed')
                # Feature 4
                with ui.row().classes('bg-white/1 p-6 rounded-2xl border border-white/5 gap-4 items-start glass-card-hover-generic transition-all duration-300'):
                    ui.element('div').classes('p-2 rounded-xl bg-indigo-500/10 border border-indigo-500/25 flex items-center justify-center') \
                        .content(ui.icon('videocam', color='indigo-400', size='xs'))
                    with ui.column().classes('gap-1 grow'):
                        ui.label('Shot-to-Text Mapping').classes('text-base font-bold text-white font-outfit')
                        ui.label('Associate virtual camera positions, focal lengths, and camera directions directly to specific script lines.').classes('text-xs text-[#A3A0B3] leading-relaxed')

        # 6. Footer Section
        with ui.column().classes('w-full max-w-[1200px] mt-28 px-6 gap-0'):
            ui.separator().classes('bg-white/5')
            with ui.row().classes('w-full py-8 flex flex-col md:flex-row justify-between items-center gap-4 text-xs text-neutral-500'):
                ui.label('© 2026 ScriptWorks Suite. All rights reserved.').classes('font-outfit')
                with ui.row().classes('items-center gap-4'):
                    ui.label('ScriptPulse').classes('cursor-pointer hover:text-white transition').on('click', lambda: ui.navigate.to('https://scriptpulse-app.streamlit.app', new_tab=True))
                    ui.label('•').classes('text-neutral-700')
                    ui.label('SceneForge').classes('cursor-pointer hover:text-white transition').on('click', lambda: ui.navigate.to('https://sceneforge-aqua-ocean.reflex.run', new_tab=True))

# ── Startup Execution ────────────────────────────────────────────────────────

ui.run(port=8550, host="127.0.0.1", show=False)
