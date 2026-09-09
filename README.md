# Codex Software Engineering Skills

[![Validate skills](https://github.com/egeetas/skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/egeetas/skills/actions/workflows/validate-skills.yml)

Reusable, safety-conscious skills for planning, building, testing, reviewing, shipping, and operating software with Codex.

[Türkçe](#türkçe) · [English](#english) · [Kurulum / Setup](SETUP.md)

## Türkçe

Bu depo, Codex'in yazılım geliştirme görevlerinde tekrar kullanılabilir ve tutarlı iş akışları izlemesini sağlayan bağımsız skill paketleri içerir. Her klasörde zorunlu bir `SKILL.md` bulunur; bazı yeni paketlerde Codex arayüz bilgileri için `agents/openai.yaml` da vardır.

Skill'ler talebi genişletmez. Kod inceleme yalnızca raporlar, kullanıcı düzeltme istemedikçe değişiklik yapmaz. Commit, push, issue/PR yayınlama, release ve deployment gibi dış işlemler açık yetki gerektirir.

### Öne çıkan iş akışları

- **Uçtan uca geliştirme:** `software-development-workflow` yalnızca gereken uzman skill'leri seçerek gereksinimden doğrulamaya kadar yönlendirir.
- **Issue'dan PR'a:** `issue-to-pr-workflow` kabul edilmiş bir issue'yu yeniden üretme, düzeltme, regresyon testi, review ve PR teslimine taşır.
- **Test ve düzeltme:** `test-and-fix-loop` formatter, lint, type-check, test ve build hatalarını sınıflandırır; doğrulanmış nedenleri düzeltir ve yeniden test eder.
- **Repo kalite denetimi:** `repo-quality-audit` testleri çalıştırır, kanıtlanabilir bug/güvenlik sorunları arar, bağımsız subagent kanalları kullanabilir ve izin verildiğinde deduplikasyonlu issue açabilir.
- **Frontend kalitesi:** `frontend-design`, `frontend-quality`, `accessibility-review`, `visual-regression` ve `webapp-testing` tasarım kararından gerçek tarayıcı doğrulamasına kadar birbirini tamamlar.
- **Teknik dokümanlar:** `technical-doc-coauthoring` RFC/ADR/spec/runbook üretir ve önemli dokümanları taze subagent'larla okuyucu gözüyle test eder.

### Skill kataloğu

#### Planlama ve mimari

- `product-requirements` — kapsam, kabul kriterleri, kapsam dışı maddeler ve edge case'ler.
- `codebase-mapping` — entrypoint, modül, veri akışı, entegrasyon ve değişiklik yüzeyi haritası.
- `architecture-decision` — alternatifler, trade-off'lar, ADR, geçiş ve rollback.
- `api-design` — tutarlı ve evrilebilir API sözleşmeleri.
- `project-bootstrap` — yeni projeler için doğrulanabilir başlangıç yapısı.

#### Uygulama, test ve teslim

- `implementation-standards` — bakımı kolay uygulama ve açık sözleşmeler.
- `change-safety` — küçük diff, uyumluluk, kullanıcı değişikliklerini koruma ve doğrulama.
- `refactoring-playbook` — davranışı koruyan, aşamalı refactoring.
- `dependency-management` — paket seçimi, CVE/lisans/unused paket ve supply-chain denetimi.
- `testing-standards` — unit, integration, contract ve E2E test standartları.
- `debugging-checklist` — repro, hipotez, izolasyon ve root-cause analizi.
- `test-and-fix-loop` — kontrolleri çalıştırıp doğrulanmış hataları güvenli biçimde düzeltme.
- `code-review` — correctness, security, performance ve regresyon incelemesi.
- `repo-quality-audit` — paralel bug avı, testler ve issue kalite kapısı.
- `issue-triage` — severity, priority, deduplikasyon ve sonraki adım.
- `issue-to-pr-workflow` — issue'dan doğrulanmış pull request'e teslim.
- `git-workflow` — branch, commit, staging, rebase/merge ve push güvenliği.
- `pr-preparation` — incelemeye hazır PR gövdesi, kanıt, risk ve rollback.
- `release-checklist` — versiyon, artifact, rollout, izleme ve rollback.
- `changelog-generator` — doğrulanmış git aralığından kullanıcı odaklı release note.

#### Frontend ve mobil

- `frontend-design` — ürüne özgü görsel yön, tipografi, layout, motion ve UI metni.
- `frontend-quality` — responsive davranış, semantik yapı ve kullanıcı durumları.
- `webapp-testing` — gerçek tarayıcıda flow, console/network, erişilebilirlik ve viewport testi.
- `accessibility-review` — erişilebilirlik incelemesi ve uygulanabilir bulgular.
- `visual-regression` — kontrollü ekran görüntüsü ve görsel değişiklik doğrulaması.
- `platform-guidelines` — platform davranışları ve tasarım sözleşmeleri.
- `device-testing` — cihaz, viewport ve çevresel davranış testi.
- `mobile-release` — mobil paketleme, mağaza ve rollout hazırlığı.

#### Güvenlik ve operasyon

- `security-baseline` — trust boundary, kimlik, input, secret ve güvenli varsayılanlar.
- `threat-modeling` — varlık, saldırı yüzeyi, tehdit ve azaltım analizi.
- `database-migrations` — geriye uyumlu şema/veri geçişleri.
- `observability-standards` — log, metric, trace ve alarm kalitesi.
- `performance-investigation` — ölçüme dayalı performans analizi.
- `incident-response` — güvenli müdahale, azaltım ve iletişim.
- `postmortem` — suçlamasız, kanıta dayalı olay analizi.

#### AI, MCP ve dokümantasyon

- `mcp-builder` — güvenli, keşfedilebilir ve test edilmiş MCP sunucuları.
- `ai-evaluation` — model/agent davranışı için tekrarlanabilir eval.
- `prompt-versioning` — prompt değişiklikleri, sürümleme ve regresyon kontrolü.
- `model-safety` — model çıktısı, tool use ve kötüye kullanım sınırları.
- `documentation-style` — README, API dokümanı, yorum ve changelog stili.
- `technical-doc-coauthoring` — RFC, ADR, spec, proposal ve runbook ortak yazımı.

### Hızlı kurulum

Codex'e şu isteği verebilirsiniz:

```text
Use $skill-installer to install skills from https://github.com/egeetas/skills
```

Ya da depoyu klonlayıp tüm skill'leri kişisel kapsamda symlink olarak kurun:

```bash
git clone https://github.com/egeetas/skills.git "$HOME/.local/share/egeetas-skills"
cd "$HOME/.local/share/egeetas-skills"
./scripts/install.sh
```

Yalnızca seçtiklerinizi kurmak için:

```bash
./scripts/install.sh frontend-design webapp-testing test-and-fix-loop
```

Ayrıntılı kişisel ve repo-kapsamlı kurulum, güncelleme ve doğrulama adımları için [SETUP.md](SETUP.md) dosyasına bakın.

### Kullanım

Codex CLI veya IDE içinde `/skills` ile keşfedin ya da skill'i açıkça çağırın:

```text
$codebase-mapping bu repoda ödeme akışını ve değişiklik yüzeyini çıkar
$test-and-fix-loop ilgili testleri çalıştır, doğrulanmış hataları düzelt
$issue-to-pr-workflow 42 numaralı issue'yu uygula ve PR'a hazırla
```

Codex ayrıca görev bir skill'in `description` alanıyla eşleştiğinde onu otomatik seçebilir.

## English

This repository provides focused, reusable Codex skills for a complete software-engineering lifecycle. Every skill is a self-contained directory with a required `SKILL.md`; selected skills also include `agents/openai.yaml` metadata for the Codex UI.

The collection preserves authorization boundaries. A review request reports findings without silently fixing them. Commits, pushes, issue/PR publication, releases, deployments, and other external mutations require explicit user authorization.

### What is included

- **Planning and architecture:** product requirements, codebase mapping, architecture decisions, API design, and project bootstrap.
- **Implementation and delivery:** implementation/change safety, refactoring, dependency audits, testing, debugging, test-and-fix, code review, repository audit, issue triage, issue-to-PR delivery, git, PR, release, and changelog workflows.
- **Frontend and mobile:** distinctive frontend design, frontend quality, real-browser testing, accessibility, visual regression, platform/device testing, and mobile release.
- **Security and operations:** security baselines, threat modeling, migrations, observability, performance investigations, incident response, and postmortems.
- **AI, MCP, and documentation:** MCP server development, AI evaluations, prompt versioning, model safety, documentation style, and reader-tested technical document coauthoring.

### Quick install

Ask Codex:

```text
Use $skill-installer to install skills from https://github.com/egeetas/skills
```

Or clone the repository and symlink all skills into your user scope:

```bash
git clone https://github.com/egeetas/skills.git "$HOME/.local/share/egeetas-skills"
cd "$HOME/.local/share/egeetas-skills"
./scripts/install.sh
```

Install a selected subset:

```bash
./scripts/install.sh frontend-design webapp-testing test-and-fix-loop
```

See [SETUP.md](SETUP.md) for user-level and repository-level installation, updates, verification, and troubleshooting.

### Invoke a skill

Use `/skills` in Codex CLI or the IDE extension, or mention a skill explicitly:

```text
$codebase-mapping map the payment flow and likely change surface
$test-and-fix-loop run the relevant checks and fix confirmed failures
$issue-to-pr-workflow implement issue 42 and prepare the pull request
```

Codex may also select a skill implicitly when the task matches its `description`.

## Development

Validate every skill locally:

```bash
python3 scripts/validate_skills.py
```

The same validation runs in GitHub Actions on pushes to `main` and on pull requests.

## License and attribution

Original work in this collection is licensed under [MIT](LICENSE). The Codex-adapted `frontend-design`, `webapp-testing`, and `mcp-builder` skills include work derived from [anthropics/skills](https://github.com/anthropics/skills) under Apache-2.0. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [LICENSES/Apache-2.0.txt](LICENSES/Apache-2.0.txt).

Official Codex skill documentation: <https://developers.openai.com/codex/skills>
