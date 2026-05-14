import streamlit as st
import time
import html as html_lib

st.set_page_config(
    page_title="ResearchMind · Multi-Agent Research",
    page_icon="◎",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');

:root {
    --void:   #060609;
    --deep:   #0d0e14;
    --panel:  #111318;
    --glass:  rgba(255,255,255,0.03);
    --rim:    rgba(255,255,255,0.07);
    --rim2:   rgba(255,255,255,0.12);
    --text:   #e2e4f0;
    --dim:    #6b6f84;
    --faint:  #2a2d3a;
    --a:      #7c6dfa;
    --b:      #38bdf8;
    --c:      #fb923c;
    --d:      #4ade80;
    --a-glow: rgba(124,109,250,0.18);
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"], .stApp {
    background: var(--void) !important;
    font-family: 'Manrope', sans-serif !important;
    color: var(--text) !important;
}

#MainMenu, footer, header, .stDeployButton { display: none !important; }
.block-container {
    padding: 0 2.2rem 1.4rem !important;
    max-width: 1320px !important;
    margin: 0 auto !important;
}

/* HERO */
.hero-center {
    text-align: center;
    padding: 2.2rem 2rem 1.4rem;
}
.hero-kicker {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.74rem;
    letter-spacing: 0.24em;
    color: var(--c);
    text-transform: uppercase;
    margin-bottom: 0.7rem;
}
.hero-title {
    font-size: clamp(3rem, 8vw, 7.2rem);
    font-weight: 700;
    line-height: 0.95;
    letter-spacing: -0.04em;
}
.hero-title .left { color: #ece8e2; }
.hero-title .right {
    background: linear-gradient(135deg, #fb923c 0%, #f97316 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    margin: 1rem auto 0;
    max-width: 820px;
    color: #9aa0b5;
    font-size: 0.96rem;
    line-height: 1.6;
}
.hero-divider {
    border: none;
    height: 1px;
    background: var(--rim);
    margin: 1.3rem auto 0;
    max-width: 1220px;
}

/* GRID */
.main-grid {
    display: grid;
    grid-template-columns: 360px 1fr;
    min-height: calc(100vh - 68px);
    background: radial-gradient(ellipse 70% 50% at 85% -10%, rgba(124,109,250,0.07) 0%, transparent 55%),
                radial-gradient(ellipse 40% 40% at -5% 90%, rgba(56,189,248,0.05) 0%, transparent 60%),
                var(--void);
}

/* LEFT */
.left-col {
    border-right: 1px solid var(--rim);
    padding: 1.8rem 2rem 2.5rem;
    display: flex;
    flex-direction: column;
    gap: 2rem;
    background: var(--deep);
}
.panel-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.54rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--dim);
    margin-bottom: 0.6rem;
}
.headline {
    font-size: 2.3rem; font-weight: 700;
    line-height: 1.08; letter-spacing: -0.035em; color: var(--text);
}
.headline em {
    font-style: normal;
    background: linear-gradient(100deg, var(--a) 0%, var(--b) 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* INPUT */
.stTextInput > div > div {
    background: var(--panel) !important;
    border: 1px solid var(--rim) !important;
    border-radius: 10px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-family: 'Manrope', sans-serif !important;
    font-size: 0.82rem !important;
    color: var(--text) !important;
    padding: 0.7rem 1rem !important;
    transition: border-color 0.25s, box-shadow 0.25s !important;
}
.stTextInput > div > div:focus-within {
    border-color: var(--a) !important;
    box-shadow: 0 0 0 3px var(--a-glow) !important;
}
.stTextInput input { color: var(--text) !important; }
.stTextInput label { color: var(--dim) !important; font-size: 0.7rem !important; letter-spacing: 0.1em !important; }
.stTextInput label { color: var(--dim) !important; font-size: 0.64rem !important; letter-spacing: 0.09em !important; }

/* BUTTON */
.stButton > button {
    width: 100% !important;
    background: linear-gradient(135deg, var(--a), #a78bfa) !important;
    color: #fff !important; border: none !important;
    border-radius: 10px !important;
    font-family: 'Manrope', sans-serif !important;
    font-weight: 600 !important; font-size: 0.8rem !important;
    letter-spacing: 0.06em !important;
    padding: 0.7rem 1.5rem !important;
    transition: opacity 0.2s, transform 0.15s !important;
}
.stButton > button:hover { opacity: 0.85 !important; transform: translateY(-1px) !important; }

/* NODES */
.agent-nodes { display: flex; flex-direction: column; gap: 0; }
.agent-node {
    display: flex; align-items: center; gap: 0.85rem;
    padding: 0.85rem 1rem;
    border-radius: 10px;
    border: 1px solid var(--rim);
    background: var(--glass);
    position: relative; overflow: hidden;
    transition: border-color 0.3s, background 0.3s;
}
.agent-node.active {
    border-color: var(--node-c) !important;
    background: rgba(var(--node-rgb), 0.06) !important;
}
.agent-node.done { border-color: rgba(var(--node-rgb), 0.28) !important; }
.node-icon {
    width: 34px; height: 34px; border-radius: 8px;
    background: rgba(var(--node-rgb), 0.1);
    border: 1px solid rgba(var(--node-rgb), 0.22);
    display: flex; align-items: center; justify-content: center;
    font-size: 0.9rem; flex-shrink: 0;
}
.agent-node.active .node-icon { animation: breathe 1.6s ease-in-out infinite; }
@keyframes breathe {
    0%,100% { box-shadow: 0 0 0 0 rgba(var(--node-rgb),0.5); }
    50%      { box-shadow: 0 0 0 7px rgba(var(--node-rgb),0); }
}
.node-info { flex: 1; min-width: 0; }
.node-name { font-size: 0.8rem; font-weight: 600; color: var(--text); }
.node-name { font-size: 0.76rem; font-weight: 600; color: var(--text); }
.node-desc { font-family: 'JetBrains Mono', monospace; font-size: 0.6rem; color: var(--dim); margin-top: 1px; }
.node-badge {
    font-family: 'JetBrains Mono', monospace; font-size: 0.52rem;
    letter-spacing: 0.1em; text-transform: uppercase;
    padding: 0.18rem 0.55rem; border-radius: 20px; flex-shrink: 0;
}
.nb-idle    { background: var(--faint); color: var(--dim); border: 1px solid var(--rim); }
.nb-running { background: rgba(124,109,250,0.12); color: var(--a); border: 1px solid rgba(124,109,250,0.4); animation: blink 1s ease-in-out infinite; }
.nb-done    { background: rgba(74,222,128,0.1); color: var(--d); border: 1px solid rgba(74,222,128,0.35); }
.nb-error   { background: rgba(248,113,113,0.1); color: #f87171; border: 1px solid rgba(248,113,113,0.35); }
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.45} }
.node-connector { width: 1px; height: 14px; background: var(--rim); margin: 0 auto 0 17px; }

/* RIGHT */
.right-col { padding: 2.5rem 3rem; display: flex; flex-direction: column; gap: 1.75rem; overflow-y: auto; }

/* TERMINAL */
.terminal {
    background: var(--panel);
    border: 1px solid var(--rim);
    border-radius: 12px; overflow: hidden;
}
.term-bar {
    display: flex; align-items: center; gap: 0.5rem;
    padding: 0.55rem 1rem;
    border-bottom: 1px solid var(--rim);
    background: rgba(255,255,255,0.018);
}
.tdot { width: 9px; height: 9px; border-radius: 50%; }
.td1{background:#ff5f56}.td2{background:#ffbd2e}.td3{background:#27c93f}
.term-label { font-family:'JetBrains Mono',monospace; font-size:0.62rem; letter-spacing:0.1em; color:var(--dim); margin-left:4px; text-transform:uppercase; }
.term-body {
    font-family: 'JetBrains Mono', monospace; font-size: 0.73rem;
    font-size: 0.67rem;
    line-height: 1.75; color: #8090b0;
    padding: 1rem 1.25rem; min-height: 110px; max-height: 240px;
    overflow-y: auto; white-space: pre-wrap; word-break: break-word;
}
.term-body::-webkit-scrollbar{width:3px}
.term-body::-webkit-scrollbar-thumb{background:var(--faint);border-radius:2px}
.ls{color:var(--dim)}.la{color:#a78bfa}.lb{color:#38bdf8}.lc{color:#fb923c}.ld{color:#4ade80}.le{color:#f87171}

/* STATS */
.stats-grid {
    display: grid; grid-template-columns: repeat(4,1fr);
    gap: 1px; background: var(--rim);
    border-radius: 12px; overflow: hidden; border: 1px solid var(--rim);
}
.stat-cell { background: var(--panel); padding: 1rem 1.2rem; }
.stat-l { font-family:'JetBrains Mono',monospace; font-size:0.58rem; letter-spacing:0.15em; text-transform:uppercase; color:var(--dim); margin-bottom:3px; }
.stat-v { font-size:1.08rem; font-weight:700; letter-spacing:-0.03em; color:var(--text); line-height:1; }
.stat-v small { font-size:0.6rem; color:var(--dim); font-weight:400; margin-left:1px; }

/* REPORT */
.report-card {
    background: var(--panel);
    border: 1px solid rgba(124,109,250,0.3);
    border-radius: 14px; overflow: hidden;
    box-shadow: 0 0 80px rgba(124,109,250,0.04);
}
.report-head { padding: 1.4rem 1.75rem 0; }
.report-eyebrow { font-family:'JetBrains Mono',monospace; font-size:0.58rem; letter-spacing:0.2em; text-transform:uppercase; color:var(--a); margin-bottom:4px; }
.report-topic { font-size:1.35rem; font-weight:700; letter-spacing:-0.025em; color:var(--text); line-height:1.2; }
.report-topic { font-size:1.22rem; font-weight:700; letter-spacing:-0.025em; color:var(--text); line-height:1.2; }
.report-divider { border:none; height:1px; background:var(--rim); margin:1.2rem 0 0; }
.report-body {
    font-size:0.78rem; line-height:1.78; color:var(--text);
    padding:1.4rem 1.75rem 1.75rem;
    white-space:pre-wrap; word-break:break-word;
    max-height:500px; overflow-y:auto;
}
.report-body::-webkit-scrollbar{width:3px}
.report-body::-webkit-scrollbar-thumb{background:rgba(124,109,250,0.3);border-radius:2px}

/* CRITIC */
.critic-card {
    background: var(--panel);
    border: 1px solid rgba(74,222,128,0.22);
    border-radius: 14px; overflow: hidden;
}
.critic-head {
    display:flex; align-items:center; gap:0.7rem;
    padding:1rem 1.4rem; border-bottom:1px solid var(--rim);
    background: rgba(74,222,128,0.03);
}
.critic-ic {
    width:28px;height:28px;border-radius:6px;
    background:rgba(74,222,128,0.1);border:1px solid rgba(74,222,128,0.22);
    display:flex;align-items:center;justify-content:center;font-size:0.85rem;
}
.critic-title { font-size:0.8rem; font-weight:600; color:var(--d); }
.critic-title { font-size:0.74rem; font-weight:600; color:var(--d); }
.critic-body {
    font-family:'JetBrains Mono',monospace; font-size:0.68rem;
    line-height:1.75; color:#8b95b3;
    padding:1.2rem 1.4rem;
    white-space:pre-wrap; word-break:break-word;
}

/* EMPTY */
.empty-state {
    display:flex; flex-direction:column; align-items:center; justify-content:center;
    height:100%; min-height:380px; gap:1rem; opacity:0.35;
}
.empty-glyph { font-family:'JetBrains Mono',monospace; font-size:2.5rem; color:var(--a); }
.empty-msg { font-family:'JetBrains Mono',monospace; font-size:0.65rem; letter-spacing:0.14em; text-transform:uppercase; color:var(--dim); text-align:center; line-height:1.8; }

/* ERROR */
.err-box {
    background:rgba(248,113,113,0.06); border:1px solid rgba(248,113,113,0.28);
    border-radius:10px; padding:1rem 1.2rem;
    font-family:'JetBrains Mono',monospace; font-size:0.73rem; color:#f87171;
    white-space:pre-wrap; line-height:1.65;
}

/* DOWNLOAD */
.stDownloadButton > button {
    background: var(--panel) !important; color:var(--text) !important;
    border:1px solid var(--rim2) !important; border-radius:8px !important;
    font-family:'Manrope',sans-serif !important; font-size:0.78rem !important;
    padding:0.45rem 1.2rem !important;
    transition:border-color 0.2s, background 0.2s !important;
}
.stDownloadButton > button:hover { border-color:var(--a) !important; background:rgba(124,109,250,0.07) !important; }
.stSpinner > div { border-top-color: var(--a) !important; }
hr { display:none !important; }
</style>
""", unsafe_allow_html=True)


# ── session defaults ──────────────────────────────────────────────────────────
for k, v in [("result",None),("error",None),("elapsed",None),("ran_topic",None),("logs",None),("statuses",None)]:
    if k not in st.session_state:
        st.session_state[k] = v
if st.session_state.statuses is None:
    st.session_state.statuses = {1:"idle",2:"idle",3:"idle",4:"idle"}


# ── helpers ───────────────────────────────────────────────────────────────────
AGENTS = [
    (1,"124,109,250","var(--a)","◈","Search Agent","tavily web search"),
    (2,"56,189,248", "var(--b)","◉","Reader Agent","scrape + extract"),
    (3,"251,146,60", "var(--c)","◎","Writer Chain","gemini synthesis"),
    (4,"74,222,128",  "var(--d)","◆","Critic Chain","evaluate report"),
]

def agent_nodes_html(statuses):
    out = '<div class="agent-nodes">'
    for i,(num,rgb,cv,icon,name,desc) in enumerate(AGENTS):
        s = statuses[num]
        ac = "active" if s=="running" else ("done" if s=="done" else "")
        out += f"""<div class="agent-node {ac}" style="--node-rgb:{rgb};--node-c:{cv};">
            <div class="node-icon">{icon}</div>
            <div class="node-info"><div class="node-name">{name}</div><div class="node-desc">{desc}</div></div>
            <div class="node-badge nb-{s}">{s}</div>
        </div>"""
        if i < 3:
            out += '<div class="node-connector"></div>'
    out += '</div>'
    return out

def log(msg, cls="ls"):
    ts = time.strftime("%H:%M:%S")
    return f'<span class="ls">[{ts}]</span> <span class="{cls}">{html_lib.escape(msg)}</span>\n'

def terminal_html(lines):
    body = "".join(lines) if lines else '<span class="ls">awaiting input...</span>'
    return f"""<div class="terminal">
    <div class="term-bar">
        <span class="tdot td1"></span><span class="tdot td2"></span><span class="tdot td3"></span>
        <span class="term-label">researchmind · system log</span>
    </div>
    <div class="term-body">{body}</div>
</div>"""


# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""<div class="hero-center">
    <div class="hero-kicker">Multi-Agent AI System</div>
    <div class="hero-title"><span class="left">Research</span><span class="right">Mind</span></div>
    <div class="hero-sub">
        Four specialized AI agents collaborate to search, scrape, write, and critique,
        delivering a polished research report for your topic.
    </div>
    <hr class="hero-divider" />
</div>""", unsafe_allow_html=True)

# ── GRID ──────────────────────────────────────────────────────────────────────
left, right = st.columns([1, 1.08], gap="large")

with left:
    st.markdown('<div class="left-col">', unsafe_allow_html=True)

    st.markdown('<div class="panel-label">Research Topic</div>', unsafe_allow_html=True)
    topic = st.text_input("TOPIC", placeholder="e.g. Quantum computing breakthroughs in 2026", label_visibility="collapsed")

    run = st.button("⟶  RUN RESEARCH PIPELINE", use_container_width=True)

    st.markdown('<div class="panel-label" style="margin-top:1rem;">Workflow</div>', unsafe_allow_html=True)
    nodes_ph = st.empty()
    nodes_ph.markdown(agent_nodes_html(st.session_state.statuses), unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="right-col">', unsafe_allow_html=True)

    term_ph    = st.empty()
    results_ph = st.empty()

    term_ph.markdown(terminal_html(st.session_state.logs or []), unsafe_allow_html=True)

    # show previous results
    if st.session_state.result and not run:
        res = st.session_state.result
        ran = st.session_state.ran_topic or ""
        elapsed = st.session_state.elapsed or 0
        sc = len(res.get("scraped_content",""))
        rc = len(str(res.get("report","")))
        with results_ph.container():
            st.markdown(f"""<div class="stats-grid">
                <div class="stat-cell"><div class="stat-l">Topic</div><div class="stat-v" style="font-size:0.82rem;">{html_lib.escape(ran[:20])}{'…' if len(ran)>20 else ''}</div></div>
                <div class="stat-cell"><div class="stat-l">Elapsed</div><div class="stat-v">{elapsed}<small>s</small></div></div>
                <div class="stat-cell"><div class="stat-l">Scraped</div><div class="stat-v">{sc:,}<small>ch</small></div></div>
                <div class="stat-cell"><div class="stat-l">Report</div><div class="stat-v">{rc:,}<small>ch</small></div></div>
            </div>""", unsafe_allow_html=True)
            if res.get("report"):
                st.markdown(f"""<div class="report-card">
                    <div class="report-head">
                        <div class="report-eyebrow">FINAL SYNTHESIS</div>
                        <div class="report-topic">{html_lib.escape(ran)}</div>
                        <div class="report-divider"></div>
                    </div>
                    <div class="report-body">{html_lib.escape(str(res["report"]))}</div>
                </div>""", unsafe_allow_html=True)
                st.download_button("↓  Download report (.txt)", data=str(res["report"]),
                    file_name=f"researchmind_{ran[:28].replace(' ','_')}.txt", mime="text/plain")
            if res.get("feedback"):
                st.markdown(f"""<div class="critic-card">
                    <div class="critic-head"><div class="critic-ic">◆</div><div class="critic-title">Critic Evaluation</div></div>
                    <div class="critic-body">{html_lib.escape(str(res["feedback"]))}</div>
                </div>""", unsafe_allow_html=True)
    elif not st.session_state.result and not run:
        results_ph.markdown("""<div class="empty-state">
            <div class="empty-glyph">◎</div>
            <div class="empty-msg">Enter a topic<br>to begin research</div>
        </div>""", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# ── PIPELINE RUN ──────────────────────────────────────────────────────────────
if run and topic.strip():
    st.session_state.update(result=None, error=None, ran_topic=topic.strip())
    results_ph.empty()
    logs = []; statuses = {1:"idle",2:"idle",3:"idle",4:"idle"}; contents = {}

    def refresh():
        nodes_ph.markdown(agent_nodes_html(statuses), unsafe_allow_html=True)
        term_ph.markdown(terminal_html(logs), unsafe_allow_html=True)

    logs += [log("researchmind pipeline initialised","ls"), log(f"topic → {topic}","la")]
    refresh(); t0 = time.time()

    # Step 1 — Search
    statuses[1]="running"; logs.append(log("search agent dispatched","la")); refresh()
    try:
        from agents import build_search_agent
        sr = build_search_agent().invoke({"messages":[("user",f"Find recent, reliable and detailed information about: {topic}")]})
        contents["search_results"] = sr["messages"][-1].content
        statuses[1]="done"
        logs.append(log(f"search complete · {len(contents['search_results']):,} chars","ld"))
    except Exception as e:
        statuses[1]="error"; contents["search_results"]=str(e)
        st.session_state.error=str(e); logs.append(log(f"search failed: {str(e)[:100]}","le"))
    refresh()

    if not st.session_state.error:
        # Step 2 — Reader
        statuses[2]="running"; logs.append(log("reader agent scraping","lb")); refresh()
        try:
            from agents import build_reader_agent
            rr = build_reader_agent().invoke({"messages":[("user",
                f"Based on the following search results about '{topic}', pick the most relevant URL and scrape it.\n\nSearch Results:\n{contents['search_results'][:800]}")]})
            contents["scraped_content"] = rr["messages"][-1].content
            statuses[2]="done"
            logs.append(log(f"scrape complete · {len(contents['scraped_content']):,} chars","ld"))
        except Exception as e:
            statuses[2]="error"; contents["scraped_content"]=str(e)
            st.session_state.error=str(e); logs.append(log(f"reader failed: {str(e)[:100]}","le"))
        refresh()

    if not st.session_state.error:
        # Step 3 — Writer
        statuses[3]="running"; logs.append(log("writer chain composing report","lc")); refresh()
        try:
            from agents import writer_chain
            combined = f"SEARCH RESULTS:\n{contents['search_results']}\n\nDETAILED SCRAPED CONTENT:\n{contents['scraped_content']}"
            contents["report"] = writer_chain.invoke({"topic":topic,"research":combined})
            statuses[3]="done"
            logs.append(log(f"report drafted · {len(str(contents['report'])):,} chars","ld"))
        except Exception as e:
            statuses[3]="error"; contents["report"]=str(e)
            st.session_state.error=str(e); logs.append(log(f"writer failed: {str(e)[:100]}","le"))
        refresh()

    if not st.session_state.error:
        # Step 4 — Critic
        statuses[4]="running"; logs.append(log("critic chain evaluating","ld")); refresh()
        try:
            from agents import critic_chain
            contents["feedback"] = critic_chain.invoke({"report":contents["report"]})
            statuses[4]="done"
            logs.append(log("critique complete · pipeline done","ld"))
        except Exception as e:
            statuses[4]="error"; contents["feedback"]=str(e)
            st.session_state.error=str(e); logs.append(log(f"critic failed: {str(e)[:100]}","le"))
        refresh()

    elapsed = round(time.time()-t0,1)
    logs.append(log(f"total elapsed: {elapsed}s","ls"))
    refresh()

    st.session_state.update(elapsed=elapsed, logs=logs, statuses=statuses, result=contents)

    ran = topic.strip()
    sc = len(contents.get("scraped_content",""))
    rc = len(str(contents.get("report","")))

    with results_ph.container():
        st.markdown(f"""<div class="stats-grid">
            <div class="stat-cell"><div class="stat-l">Topic</div><div class="stat-v" style="font-size:0.82rem;">{html_lib.escape(ran[:20])}{'…' if len(ran)>20 else ''}</div></div>
            <div class="stat-cell"><div class="stat-l">Elapsed</div><div class="stat-v">{elapsed}<small>s</small></div></div>
            <div class="stat-cell"><div class="stat-l">Scraped</div><div class="stat-v">{sc:,}<small>ch</small></div></div>
            <div class="stat-cell"><div class="stat-l">Report</div><div class="stat-v">{rc:,}<small>ch</small></div></div>
        </div>""", unsafe_allow_html=True)

        if st.session_state.error:
            st.markdown(f'<div class="err-box">⚠ ERROR\n\n{html_lib.escape(st.session_state.error)}</div>', unsafe_allow_html=True)

        if contents.get("report"):
            st.markdown(f"""<div class="report-card">
                <div class="report-head">
                    <div class="report-eyebrow">FINAL SYNTHESIS</div>
                    <div class="report-topic">{html_lib.escape(ran)}</div>
                    <div class="report-divider"></div>
                </div>
                <div class="report-body">{html_lib.escape(str(contents["report"]))}</div>
            </div>""", unsafe_allow_html=True)
            st.download_button("↓  Download report (.txt)", data=str(contents["report"]),
                file_name=f"researchmind_{ran[:28].replace(' ','_')}.txt", mime="text/plain")

        if contents.get("feedback"):
            st.markdown(f"""<div class="critic-card">
                <div class="critic-head"><div class="critic-ic">◆</div><div class="critic-title">Critic Evaluation</div></div>
                <div class="critic-body">{html_lib.escape(str(contents["feedback"]))}</div>
            </div>""", unsafe_allow_html=True)

elif run and not topic.strip():
    st.warning("Enter a research topic first.")
