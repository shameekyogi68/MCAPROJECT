# ScriptPulse Brand Kit & Design System
*Version 1.0 — Writer-First Story Intelligence*

This document outlines the core brand identity, typography, color palette, and premium UI design specifications for the **ScriptPulse** application, conforming to the **Tactile Glass / Premium Instrument** design language.

---

## 1. Brand Philosophy
ScriptPulse is designed to feel like a high-precision, premium instrument for screenwriters and story editors. It follows three creative principles:
* **Writer-First Respect**: Diagnostics represent reflection signals, never judgmental metrics (no "good" or "bad" labels).
* **Tactile Glass Aesthetic**: Depth is achieved via semi-transparent layers, frosted backdrops, and physical-like shadows.
* **Functional Radiance**: Bright brand colors are used restrictively to highlight data shifts and statuses, keeping the general dashboard dark and immersive.

---

## 2. Typography
Typography is highly structured to maintain absolute readability and professional hierarchy.

| Usage | Font Family | Weights | Letter Spacing | Color |
| :--- | :--- | :--- | :--- | :--- |
| **Main Headings (H1, H2, Title)** | `'Outfit', sans-serif` | `700` (Bold), `800` (Extra Bold) | `-0.03em` | `#FFFFFF` |
| **UI Numbers & Metrics** | `'Outfit', sans-serif` | `800` (Extra Bold) | `-0.02em` | `#FFFFFF` |
| **Body & UI Text** | `'Inter', sans-serif` | `400` (Regular), `500` (Medium), `600` (Semi-Bold) | `0` | `#E0E0E0` |
| **Subheadings & Labels** | `'Inter', sans-serif` | `700` (Bold, Uppercase) | `0.12em` | `#9E9E9E` |
| **Screenplay/Code Data** | `'JetBrains Mono', monospace` | `400` (Regular) | `0` | `#E0E0E0` |

---

## 3. Color Palette

### Core Backgrounds
* **Obsidian Black (Primary App BG)**: `#121212` (RGB: `18, 18, 18`)
* **Dark Well / Secondary Base**: `#1E1E1E` (RGB: `30, 30, 30`)
* **Glass Container Background**: `rgba(255, 255, 255, 0.03)`

### Brand Accents
* **Amethyst (Primary Brand Color)**: `#9B51E0` (RGB: `155, 81, 224`) — Used for primary actions and hero gradients.
* **Amethyst Glow**: `rgba(155, 81, 224, 0.4)`
* **Violet Accent**: `#A56DFF` (RGB: `165, 109, 255`) — Used for complex arcs and loading screen gradients.

### Semantic & Status Colors
* **Emerald Green (Positive Progression / High Agency)**: `#00C853` (RGB: `0, 200, 83`)
  * *Glass Tint*: `rgba(0, 200, 83, 0.05)`
* **Coral Orange (Neutral / Mid Agency / Warning)**: `#FF7043` (RGB: `255, 112, 67`)
  * *Glass Tint*: `rgba(255, 112, 67, 0.05)`
* **Rose Red (Negative Progression / Low Agency / Critical)**: `#FF3366` (RGB: `255, 51, 102`)
  * *Glass Tint*: `rgba(255, 51, 102, 0.05)`
* **Soft Cyan/Blue (Tragic / Redemptive / Information)**: `#55E0FF` (RGB: `85, 224, 255`)
  * *Glass Tint*: `rgba(85, 224, 255, 0.05)`

---

## 4. UI Components Specification

### The Glass Card (`.glass-card`)
A standard floating container with a frosted glass look.
```css
background: rgba(255, 255, 255, 0.03) !important;
backdrop-filter: blur(24px) !important;
-webkit-backdrop-filter: blur(24px) !important;
border: 1px solid rgba(255, 255, 255, 0.08) !important;
border-radius: 24px !important;
box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4) !important;
transition: all 0.3s ease !important;
```

### Hardware Shimmer Overlay (`.hardware-metric::after`)
Adds a glossy shine gradient on top of cards.
```css
content: '' !important;
position: absolute !important;
top: 0 !important; left: 0 !important; right: 0 !important; bottom: 0 !important;
background: linear-gradient(180deg, rgba(255, 255, 255, 0.03) 0%, transparent 100%) !important;
pointer-events: none !important;
border-radius: inherit !important;
```

### Color-Coded Rows (`.insight-item` / `.scene-turn-row`)
List items styled with 3D margins, left accent borders, and dynamic background tints:
```css
border-left: 3px solid {accent_color};
border-top: 1px solid rgba(255, 255, 255, 0.04);
border-right: 1px solid rgba(255, 255, 255, 0.03);
border-bottom: 1px solid rgba(255, 255, 255, 0.03);
background: rgba({accent_color_rgb}, 0.05);
backdrop-filter: blur(24px);
-webkit-backdrop-filter: blur(24px);
box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);
transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.2s ease;
```

### Micro-Animations
* **Card Hover Lift**: Translates vertically (`transform: translateY(-2px)`) and deepens the drop shadow (`box-shadow: 0 12px 48px rgba(0, 0, 0, 0.5)`).
* **Row Hover Slide**: Slid horizontally (`transform: translateX(4px)`) and brightens the background tint opacity to `0.08` upon hover.
