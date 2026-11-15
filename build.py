"""Generate six HTML pages while preserving owner-entered legal-name fields."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def page(*, lang, section, root, title, description, eyebrow, heading, intro, body, toc="", draft=False):
    zh = lang == "zh-CN"
    home = root or "./"
    support = root + "support/"
    privacy = root + "privacy/"
    if not zh:
        home += "en/"
        support = root + "en/support/"
        privacy = root + "en/privacy/"
    counterpart = {
        ("zh-CN", "home"): root + "en/",
        ("zh-CN", "support"): root + "en/support/",
        ("zh-CN", "privacy"): root + "en/privacy/",
        ("en-US", "home"): root,
        ("en-US", "support"): root + "support/",
        ("en-US", "privacy"): root + "privacy/",
    }[(lang, section)]
    nav = [(home, "首页" if zh else "Home", "home"),
           (support, "技术支持" if zh else "Support", "support"),
           (privacy, "隐私政策" if zh else "Privacy", "privacy")]
    nav_html = "".join(f'<a href="{href}"' + (' aria-current="page"' if key == section else '') + f'>{label}</a>' for href, label, key in nav)
    current = {"home": home, "support": support, "privacy": privacy}[section]
    lang_html = (f'<a href="{current}" aria-current="page">中文</a><span class="divider">/</span><a href="{counterpart}" lang="en-US">English</a>' if zh
                 else f'<a href="{counterpart}" lang="zh-CN">中文</a><span class="divider">/</span><a href="{current}" aria-current="page">English</a>')
    content = (body if section == "home" else f'<header class="page-head"><div class="shell"><p class="eyebrow">{eyebrow}</p><h1>{heading}</h1><p>{intro}</p></div></header><div class="shell content-layout"><article class="prose">{body}</article>{toc}</div>')
    return f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{description}">
  {('<meta name="robots" content="noindex, nofollow">' if draft else '')}
  <meta name="theme-color" content="#f7f7ef">
  <title>{title}</title>
  <link rel="icon" href="data:,">
  <link rel="stylesheet" href="{root}assets/css/site.css">
</head>
<body>
<a class="skip" href="#main">{'跳转到正文' if zh else 'Skip to content'}</a>
<header class="topbar"><div class="shell"><a class="brand" href="{home}">Shixu <span>时序</span></a><nav class="nav" aria-label="{'主导航' if zh else 'Main navigation'}">{nav_html}</nav><nav class="lang" aria-label="{'语言切换' if zh else 'Language'}">{lang_html}</nav></div></header>
<main id="main">{content}</main>
<footer class="footer"><div class="shell"><div><strong>Shixu · 时序</strong><p>{'让重要时刻清晰可见。' if zh else 'A clear view of the moments that matter.'}</p></div><nav class="footer-links" aria-label="{'页脚导航' if zh else 'Footer navigation'}"><a href="{support}">{'技术支持' if zh else 'Support'}</a><a href="{privacy}">{'隐私政策' if zh else 'Privacy policy'}</a></nav></div></footer>
</body>
</html>
'''


def toc(items, zh):
    title = "本页内容" if zh else "On this page"
    links = "".join(f'<a href="#{anchor}">{label}</a>' for anchor, label in items)
    return f'<nav class="toc" aria-label="{title}"><strong>{title}</strong>{links}</nav>'


def faq(items):
    return "".join(f'<details><summary>{question}</summary>{answer}</details>' for question, answer in items)


zh_home = '''<section class="hero"><div class="shell hero-inner"><p class="eyebrow">时间，值得被好好看见</p><h1>把重要日子<br><span>放在眼前。</span></h1><p class="lede">时序是一款专注于日期倒计时与精确计时的 iPhone App。记住值得期待的日子，也照看正在进行的每一秒。</p><div class="actions"><a class="button" href="support/">查看使用帮助</a><a class="button secondary" href="privacy/">了解隐私处理</a></div></div></section><section class="section alt"><div class="shell"><div class="section-head"><p class="eyebrow">两种时间视角</p><h2>按日历规划，按秒计时</h2><p>不同的时间任务，使用合适的方式呈现。</p></div><div class="grid"><div class="card"><div class="icon" aria-hidden="true">◷</div><h3>日期倒计时</h3><p>为生日、工作和生活中的重要日子建立记录，按自然日查看剩余时间；可使用事件样式、收藏与归档。</p></div><div class="card"><div class="icon sea" aria-hidden="true">◴</div><h3>精确计时器</h3><p>按时长或目标时间开始计时，精确到秒。可同时管理多个计时器，并按适用模式暂停、继续或循环。</p></div><div class="card"><div class="icon" aria-hidden="true">▦</div><h3>桌面小组件</h3><p>使用独立的日期与计时器小组件，在 iPhone 主屏快速查看关心的时间。刷新由 iOS 安排，可能存在延迟。</p></div></div></div></section><section class="section"><div class="shell"><div class="cta"><div><h2>需要帮助？</h2><p>查看常见问题、提醒设置和小组件使用说明。</p></div><a class="button" href="support/">前往技术支持</a></div></div></section>'''

en_home = '''<section class="hero"><div class="shell hero-inner"><p class="eyebrow">Make time visible</p><h1>Keep the moments<br><span>that matter in view.</span></h1><p class="lede">Shixu is an iPhone app for date countdowns and precise timers. Look forward to important days and keep track of every second in between.</p><div class="actions"><a class="button" href="support/">Get help</a><a class="button secondary" href="privacy/">Read our privacy policy</a></div></div></section><section class="section alt"><div class="shell"><div class="section-head"><p class="eyebrow">Two ways to see time</p><h2>Plan by day. Time by second.</h2><p>Choose the view that fits what you are tracking.</p></div><div class="grid"><div class="card"><div class="icon" aria-hidden="true">◷</div><h3>Date countdowns</h3><p>Keep birthdays, work milestones, and other dates in one place. See remaining calendar days, choose an event style, mark favorites, and archive records.</p></div><div class="card"><div class="icon sea" aria-hidden="true">◴</div><h3>Precise timers</h3><p>Start with a duration or an end time and count down to the second. Manage multiple timers, with pause, resume, and repeat where supported.</p></div><div class="card"><div class="icon" aria-hidden="true">▦</div><h3>Home Screen widgets</h3><p>Separate date and timer widgets make key information easy to glance at. iOS controls when widgets refresh, so updates may be delayed.</p></div></div></div></section><section class="section"><div class="shell"><div class="cta"><div><h2>Need a hand?</h2><p>Find answers about countdowns, reminders, and widgets.</p></div><a class="button" href="support/">Visit support</a></div></div></section>'''

zh_support_items = [
    ("如何创建日期倒计时？", '<p>在首页选择新增日期记录，输入名称和目标日期，再按需填写备注、选择事件样式与提醒。保存后，剩余天数按日历自然日计算；“明天”显示 1 天，即使距离目标时刻不足 24 小时。</p>'),
    ("如何编辑日期、名称或事件样式？", '<p>打开已有日期记录，进入编辑后修改名称、目标日期、备注或事件样式，再保存。事件样式用于区分生日、健康、工作等主题的图标与颜色，不改变倒计时的计算规则。</p>'),
    ("收藏、长期计划和归档有什么区别？", '<p>收藏便于筛选与优先显示在日期小组件中。较远的日期可能按设置进入“长期计划”；到期日期可按设置留在首页或进入“已到期”。手动归档的日期可在归档中查看和恢复。</p>'),
    ("删除后还能恢复吗？", '<p>普通删除会把日期记录或计时器移到“已删除”，可从那里恢复。只有在“已删除”中选择永久删除，才会将其从当前记录移除。有关本地恢复备份的保留边界，请参阅隐私政策。</p>'),
    ("如何创建按时长计时器（Duration）？", '<p>进入“计时器”，新增计时器并选择“按时长”，设置所需时长后开始。计时按真实秒数运行；离开 App 不会使计时停止。支持同时保存和管理多个计时器。</p>'),
    ("如何使用按目标时间（End Time）模式？", '<p>新增计时器时选择“按目标时间”，设定未来的结束时间后开始。成功开始后，记录会保留创建时的模式；若要改用另一种模式，请新建计时器。</p>'),
    ("计时器可以暂停、继续或循环吗？", '<p>按时长计时和循环目标时间计时可暂停与继续；继续时结束时刻会随冻结的剩余时长后移。非循环的目标时间计时保持固定目标，不提供暂停或继续，可选择停止或编辑。循环计时需在创建或编辑时启用适用的循环选项。</p>'),
    ("为什么没有收到提醒？", '<p>检查“设置”的总提醒开关、记录自己的提醒开关，以及 iOS 对“时序”的通知权限。日期提醒安排在目标日当地时间 09:00，超过该时间开启不会补发；计时器须处于适用的运行状态，且结束时刻仍在未来。通知的实际呈现还受 iOS 设置影响。</p>'),
    ("如何使用自定义计时铃声？", '<p>在“设置”中导入音频文件并选用作计时结束通知铃声。支持 MP3、AAC/M4A、WAV 和 CAF，单段须少于 30 秒且包含有效音轨，最多保存 5 个。自定义铃声只用于计时器结束通知，不改变日期提醒声音。</p>'),
    ("如何添加日期小组件？", '<p>在 iPhone 主屏打开系统“小组件图库”，查找“时序”，选择小号日期小组件。它最多显示 3 条仍在进行中的日期倒计时；收藏项目优先进入候选，点按可打开 App 首页。</p>'),
    ("如何添加计时器小组件？", '<p>在同一“小组件图库”中选择小号计时器小组件。它一次显示 1 个计时器；点按可打开对应计时器详情。小组件只读，不能直接暂停、继续或停止计时器。</p>'),
    ("小组件没有及时更新怎么办？", '<p>先打开时序查看记录当前状态，确认记录仍符合显示条件，再返回主屏。App 会请求刷新小组件，但最终更新时间由 iOS 安排；跨日、计时状态变化和循环跨轮可能出现延迟。若仍未显示，可尝试移除后重新添加小组件。</p>'),
]

en_support_items = [
    ("How do I create a date countdown?", '<p>On Home, add a date record, enter a name and target date, then optionally add a note, event style, or reminder. Remaining days are calendar days: tomorrow shows as 1 day even if it is less than 24 hours away.</p>'),
    ("How do I edit a date or event style?", '<p>Open the date record, choose Edit, update its name, target date, note, or event style, and save. Event styles distinguish themes such as birthdays, health, and work with icons and colors. They do not change the countdown calculation.</p>'),
    ("What do favorites, long-term plans, and archives do?", '<p>Favorites help you filter records and get priority in the date widget. Distant dates may appear under Long-Term Plans, depending on your settings. Expired dates can stay on Home or move to Expired. Manually archived dates can be viewed and restored from Archive.</p>'),
    ("Can I recover a deleted record?", '<p>A regular delete moves a date or timer to Recently Deleted, where you can restore it. Permanent Delete removes it from current records. See the privacy policy for the limits of local recovery copies.</p>'),
    ("How do I create a Duration timer?", '<p>Open Timers, add a timer, choose Duration, set the length, and start. It counts down using real elapsed seconds and keeps running when you leave the app. You can manage multiple timers.</p>'),
    ("How does End Time mode work?", '<p>When adding a timer, choose End Time and set a future target time. Once started, the timer keeps its original input mode. Create a new timer if you need the other mode.</p>'),
    ("Can I pause, resume, or repeat a timer?", '<p>Duration timers and repeating End Time timers can pause and resume. Resuming shifts the end time by the frozen remaining duration. A nonrepeating End Time timer has a fixed target and cannot pause or resume; you can stop or edit it. Enable repeating where the timer setup offers that option.</p>'),
    ("Why did I not receive a reminder?", '<p>Check the main reminders switch in Settings, the record’s reminder switch, and iOS notification permission for Shixu. Date reminders are scheduled once for 9:00 a.m. local time on the target date; enabling them later will not send a missed alert. A timer reminder requires a qualifying running timer with a future end time. iOS settings also affect delivery.</p>'),
    ("How do custom timer sounds work?", '<p>In Settings, import audio and select it for timer completion alerts. MP3, AAC/M4A, WAV, and CAF files are supported. Each must have a valid audio track and be under 30 seconds; you can keep up to five. Custom sounds apply to timer alerts, not date reminders.</p>'),
    ("How do I add a date widget?", '<p>Open the iPhone Home Screen widget gallery, find Shixu, and add the small date widget. It shows up to three active date countdowns, prioritizing favorites for selection. Tap it to open Home.</p>'),
    ("How do I add a timer widget?", '<p>In the same widget gallery, add the small timer widget. It shows one timer at a time; tap it to open that timer’s details. The widget is read-only, so timer controls remain in the app.</p>'),
    ("What if a widget has not updated?", '<p>Open Shixu to check the record’s current state and whether it still qualifies for the widget, then return to the Home Screen. The app requests widget updates, but iOS chooses the refresh time. Day changes, timer state changes, and repeat boundaries can be delayed. If needed, remove and add the widget again.</p>'),
]

zh_support = '''<section id="overview"><h2>关于时序</h2><p>时序在一处管理日期倒计时与精确计时器。日期记录按自然日计算；计时器按真实秒数运行。App 提供简体中文和美式英文界面，并有独立的日期与计时器小组件。</p><div class="notice"><strong>需要联系支持？</strong><br>正式支持邮箱：<a href="mailto:grippe-bearded9p@icloud.com">grippe-bearded9p@icloud.com</a>。</div></section><section id="dates"><h2>日期倒计时与记录管理</h2>''' + faq(zh_support_items[:4]) + '''</section><section id="timers"><h2>精确计时器与提醒</h2>''' + faq(zh_support_items[4:9]) + '''</section><section id="widgets"><h2>桌面小组件</h2>''' + faq(zh_support_items[9:]) + '''</section><section id="contact"><h2>反馈与联系</h2><p>技术支持与隐私咨询共用邮箱：<a href="mailto:grippe-bearded9p@icloud.com">grippe-bearded9p@icloud.com</a>。提出问题时，可说明 iPhone 型号、iOS 版本、时序版本和复现步骤；请自行决定是否提供截图或其他可能包含私人内容的资料。</p></section>'''

en_support = '''<section id="overview"><h2>About Shixu</h2><p>Shixu manages date countdowns and precise timers in one place. Dates use calendar days; timers use elapsed seconds. The app supports Simplified Chinese and U.S. English, with separate date and timer widgets.</p><div class="notice"><strong>Need to contact support?</strong><br>Official support email: <a href="mailto:grippe-bearded9p@icloud.com">grippe-bearded9p@icloud.com</a>.</div></section><section id="dates"><h2>Date countdowns and records</h2>''' + faq(en_support_items[:4]) + '''</section><section id="timers"><h2>Timers and reminders</h2>''' + faq(en_support_items[4:9]) + '''</section><section id="widgets"><h2>Home Screen widgets</h2>''' + faq(en_support_items[9:]) + '''</section><section id="contact"><h2>Feedback and contact</h2><p>Support and privacy inquiries share this email address: <a href="mailto:grippe-bearded9p@icloud.com">grippe-bearded9p@icloud.com</a>. When reporting a problem, you may include your iPhone model, iOS version, Shixu version, and steps to reproduce it. Share screenshots or other potentially private material only if you choose to.</p></section>'''

zh_privacy = '''<section id="scope"><h2>1. 适用范围与版本</h2><p>本政策适用于 iPhone App“时序”（Shixu）1.0.0 (8)，涵盖主 App 及其日期、计时器小组件。Shixu 由个人独立开发者运营，不属于公司或其他注册企业主体。运营者：<span data-operator-name>木槿（Shixu 独立开发者）</span>。生效日期：2026 年 11 月 15 日。</p></section>
<section id="data"><h2>2. 用户输入与本地处理的数据</h2><p>你可以在 App 内创建日期倒计时和计时器。记录可能包含你填写的名称、目标日期或时间、备注、事件样式、收藏、归档及提醒选择，以及计时状态。你填写的文字可能包含个人信息；请按自己的需要输入。</p><p>你还可以主动导入音频作为自定义计时铃声。App 会读取所选文件、检查音轨和时长，并转换成适用于本地通知的音频文件；相关名称和选择状态保存在本机设置中。</p><p>这些处理用于显示倒计时和计时器、保存你的设置、安排你开启的提醒，以及展示小组件。</p></section>
<section id="storage"><h2>3. 本地存储与小组件共享</h2><p>当前实现将日期和计时器记录、设置写入 App 在本机的 UserDefaults；转换后的自定义铃声文件保存在 App 的本地 Library/Sounds 目录。主 App 与小组件通过同一设备上的 App Group 共享显示所需的摘要：日期摘要可包含名称、目标日期和收藏等信息；计时器摘要可包含名称、起止时间与运行状态。小组件不直接读取完整记录库。</p><p>当前 App 未实现自身的 iCloud 或其他跨设备同步。设备的系统备份可能包含 App 数据；系统备份与 App 自行同步是不同机制，是否备份以及如何恢复取决于你的设备和系统设置。</p></section>
<section id="notifications"><h2>4. 本地通知</h2><p>当你开启相应提醒且授予 iOS 通知权限时，App 会通过 iOS 本地通知安排提醒。日期通知可使用事件名称作为标题；计时结束通知可包含计时器名称，并可使用你选择的本地铃声。关闭提醒或撤销权限会影响后续通知。通知由设备上的系统服务处理；这不等于将记录上传至开发者服务器。</p></section>
<section id="services"><h2>5. 网络、第三方服务与开发者收集</h2><p>本版本未提供用户账号、App 自行实现的云同步、广告、分析、追踪或崩溃上报功能，也未集成第三方网络 SDK。App 未设计主动向开发者服务器发送日期或计时器记录的功能。iOS 系统级备份和用户主动发送的支持邮件分别按本政策其他章节说明。</p></section>
<section id="deletion"><h2>6. 删除、备份与恢复</h2><p>普通删除会把记录移至 App 内“已删除”，你可以恢复。只有从“已删除”中选择永久删除，才会将记录从当前记录中移除。每次成功保存记录变更前，App 会把变更前的当前记录写入本机恢复备份。因此，永久删除后，该备份仍可能含有被删除的记录；后续再次成功保存记录变更时，备份才会被新的上一版本覆盖。当前实现没有按时间或按删除动作清除该备份的机制。</p><p>如果主记录读取失败，并且你确认使用有效备份恢复，App 会先将读取失败的主记录写入本机隔离副本。当前实现没有自动清除隔离副本的机制；它可能在后续记录删除或保存后继续保留历史内容。</p><p>在 App 设置中删除自定义铃声时，铃声会先从列表移除并标记为待清理。App 重建本地通知后，如没有待处理通知引用该文件，会尝试删除；如果清理未完成或失败，文件可能暂时保留，并在后续通知重建时再次尝试。记录变更后，App 会请求更新同设备的 Widget 摘要并重建本地通知；写入或系统刷新可能延迟或失败，因此旧摘要或待处理通知不保证立即消失。卸载 App 通常会移除其设备本地容器，但系统设备备份可能保留独立副本，受 iOS 的备份与保留设置控制。本政策不承诺所有副本同步、即时删除。</p></section>
<section id="contact"><h2>7. 主动联系支持与隐私请求</h2><p>当前 App 未内置反馈上传功能。你主动发送的技术支持或隐私咨询邮件由运营者本人接收、阅读和处理，仅用于答复咨询、排查故障及处理隐私请求。邮件可能包含你主动提供的发件邮箱、问题描述、截图和附件；我们不会主动要求你提交不必要的敏感个人信息。邮件不用于广告营销，也不会自动转发给第三方 AI 或分析服务。问题解决后，开发者会根据实际需要删除不再必要的邮件；如适用法律要求保留某些邮件或记录，则按相关要求处理。我们不设固定的 90 天保留期限，也没有自动客服、自动回复或自动删除机制。</p><p>你可以在 App 中查看、修改、删除当前记录，并通过正式隐私联系渠道提出数据处理相关问题。隐私咨询邮箱（与技术支持共用）：<a href="mailto:grippe-bearded9p@icloud.com">grippe-bearded9p@icloud.com</a>。若问题涉及设备备份，请同时查看 iOS 的备份设置。</p></section>
<section id="updates"><h2>8. 政策更新</h2><p>当 App 的功能或数据处理方式变化时，我们将更新本页面并标明新的生效日期。</p></section>'''

en_privacy = '''<section id="scope"><h2>1. Scope and version</h2><p>This policy applies to version 1.0.0 (8) of the Shixu iPhone app, including the app and its date and timer widgets. Shixu is operated by an individual independent developer, not a company or other registered business entity. Operator: <span data-operator-name>木槿（Independent Developer of Shixu）</span>. Effective date: November 15, 2026.</p></section>
<section id="data"><h2>2. Information you enter and local processing</h2><p>You can create date countdowns and timers in the app. Records may contain names, target dates or times, notes, event styles, favorites, archive status, reminder choices, and timer state. Text you enter may contain personal information; you decide what to include.</p><p>You may also import audio for a custom timer sound. The app reads the selected file, checks its audio track and duration, and converts it into a file for local notifications. Its name and selection status are stored in local settings.</p><p>The app processes this information to display countdowns and timers, save your settings, schedule reminders you enable, and show widgets.</p></section>
<section id="storage"><h2>3. Local storage and widget sharing</h2><p>The current app stores date and timer records and settings in its local UserDefaults. Converted custom sounds are stored in the app’s local Library/Sounds directory. The main app shares the summaries needed for display with its widgets through an App Group on the same device. Date summaries may include names, target dates, and favorite status; timer summaries may include names, start and end times, and running state. Widgets do not read the full record store directly.</p><p>The current app does not implement its own iCloud or other cross-device sync. Device-level system backups may include app data. System backup and app-managed sync are separate mechanisms; backup and restoration depend on your device and system settings.</p></section>
<section id="notifications"><h2>4. Local notifications</h2><p>If you enable a reminder and grant iOS notification permission, the app schedules a local notification through iOS. A date notification may use an event name as its title. A timer completion alert may include the timer name and use a locally selected sound. Turning off reminders or revoking permission affects future alerts. Processing by the device’s notification system does not mean the record is uploaded to a developer server.</p></section>
<section id="services"><h2>5. Network services, third parties, and developer collection</h2><p>This version does not offer user accounts, app-managed cloud sync, ads, analytics, tracking, or crash reporting, and it does not integrate third-party network SDKs. The app is not designed to send date or timer records to a developer server. iOS system backups and emails you choose to send to support are described separately in this policy.</p></section>
<section id="deletion"><h2>6. Deletion, backup, and recovery</h2><p>Regular deletion moves a record to Recently Deleted, where you can restore it. Permanent Delete is available there and removes the record from current records. Before each successful record change, the app writes the previous current records to a local recovery backup. After Permanent Delete, that backup may therefore still contain the deleted record. A later successful record change replaces the backup with the newer previous version. The current implementation has no timed or deletion-specific cleanup for this backup.</p><p>If the main records cannot be read and you confirm restoration from a valid backup, the app first stores the unreadable main data in a local quarantine copy. The current implementation has no automatic cleanup for this copy; it may retain historical content after later record changes or deletions.</p><p>Deleting a custom sound in the app’s settings first removes it from the list and marks its file for cleanup. After rebuilding local notifications, the app attempts to delete the file if no pending notification references it. If cleanup is incomplete or fails, the file may remain temporarily and be retried when notifications are rebuilt later. After record changes, the app requests an update to same-device widget summaries and rebuilds local notifications. Writes or system refreshes may be delayed or fail, so older summaries or pending notifications are not guaranteed to disappear immediately. Uninstalling the app normally removes its local device container, but system device backups may retain separate copies under iOS backup and retention settings. This policy does not promise immediate deletion of every copy.</p></section>
<section id="contact"><h2>7. Contacting support and privacy requests</h2><p>The current app has no built-in feedback upload feature. The operator personally receives, reads, and handles support and privacy emails you choose to send, solely to answer questions, troubleshoot problems, and address privacy requests. These emails may contain your sender address, problem description, screenshots, and attachments that you provide. We do not ask you to send unnecessary sensitive personal information. Emails are not used for advertising and are not automatically forwarded to third-party AI or analytics services. After an issue is resolved, the developer deletes emails that are no longer needed as appropriate; records may be retained where applicable law requires it. There is no fixed 90-day retention period and no automated support, auto-reply, or automatic deletion system.</p><p>You can view, edit, and delete current records in the app and ask questions about data handling through the official privacy contact channel. Privacy contact email (shared with support): <a href="mailto:grippe-bearded9p@icloud.com">grippe-bearded9p@icloud.com</a>. For device backups, also review your iOS backup settings.</p></section>
<section id="updates"><h2>8. Policy changes</h2><p>When app features or data handling change, we will update this page and show the new effective date.</p></section>'''


PAGES = [
    ("index.html", dict(lang="zh-CN", section="home", root="", title="时序 Shixu｜日期倒计时与精确计时", description="时序是一款 iPhone 日期倒计时与精确计时器 App，提供日期和计时器小组件。", eyebrow="", heading="", intro="", body=zh_home)),
    ("en/index.html", dict(lang="en-US", section="home", root="../", title="Shixu | Date Countdowns & Precise Timers", description="Shixu is an iPhone app for date countdowns, precise timers, and Home Screen widgets.", eyebrow="", heading="", intro="", body=en_home)),
    ("support/index.html", dict(lang="zh-CN", section="support", root="../", title="技术支持｜时序 Shixu", description="时序技术支持：日期倒计时、精确计时器、提醒和桌面小组件常见问题。", eyebrow="帮助中心", heading="技术支持", intro="了解日期、计时器、提醒和小组件的使用方式。", body=zh_support, toc=toc([("overview","产品简介"),("dates","日期倒计时"),("timers","计时器与提醒"),("widgets","桌面小组件"),("contact","联系支持")], True))),
    ("en/support/index.html", dict(lang="en-US", section="support", root="../../", title="Support | Shixu", description="Shixu support: answers about date countdowns, precise timers, reminders, and widgets.", eyebrow="Help center", heading="Support", intro="Find practical answers for countdowns, timers, reminders, and widgets.", body=en_support, toc=toc([("overview","Overview"),("dates","Date countdowns"),("timers","Timers & reminders"),("widgets","Widgets"),("contact","Contact")], False))),
    ("privacy/index.html", dict(lang="zh-CN", section="privacy", root="../", title="隐私政策｜时序 Shixu", description="时序隐私政策，说明数据存储、小组件共享、本地通知和删除行为。", eyebrow="隐私说明", heading="隐私政策", intro="适用于时序 1.0.0 (8)；2026 年 11 月 15 日生效。", body=zh_privacy, toc=toc([("scope","适用范围"),("data","本地处理"),("storage","存储与共享"),("notifications","通知"),("services","第三方服务"),("deletion","删除与备份"),("contact","联系与权利"),("updates","政策更新")], True))),
    ("en/privacy/index.html", dict(lang="en-US", section="privacy", root="../../", title="Privacy Policy | Shixu", description="Shixu privacy policy covering data storage, widgets, notifications, and deletion.", eyebrow="Privacy", heading="Privacy Policy", intro="Applies to Shixu 1.0.0 (8); effective November 15, 2026.", body=en_privacy, toc=toc([("scope","Scope"),("data","Local processing"),("storage","Storage & sharing"),("notifications","Notifications"),("services","Third parties"),("deletion","Deletion & backup"),("contact","Contact & rights"),("updates","Changes")], False))),
]

for name, kwargs in PAGES:
    target = ROOT / name
    target.parent.mkdir(parents=True, exist_ok=True)
    html = page(**kwargs)
    target.write_text(html, encoding="utf-8")

