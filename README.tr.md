# Codex Mühendislik Skill'leri

[![Skill doğrulama](https://github.com/egeetas/skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/egeetas/skills/actions/workflows/validate-skills.yml)
[![MIT Lisansı](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Codex skill](https://img.shields.io/badge/Codex_skills-49-111827.svg)](CATALOG.md)

Belirsiz bir ürün fikrinden uygulama, doğrulama, release ve operasyon aşamalarına kadar yazılım geliştirmeyi kapsayan 49 odaklı Codex skill'inden oluşan production-minded bir koleksiyon.

[English](README.md) · [Katalog](CATALOG.md) · [Kurulum](SETUP.tr.md) · [Skill yazım rehberi](docs/skill-authoring.md) · [Değişiklikler](CHANGELOG.md)

## Neden bu koleksiyon?

- Tek bir dev prompt yerine tüm geliştirme döngüsünü kapsayan ayrık iş akışları.
- Öngörülebilir keşif için kısa açıklamalar, 147 skill vakası ve odaklı sınır vakaları.
- Düzeltme, yayınlama, deployment ve silme gibi işlemler için açık yetki sınırları.
- Taşınabilir plugin metadata'sı, bağımsız kurulum, doğrulama, CI ve isteğe bağlı subagent preset'leri.
- Tekrarlanabilirliği artıran script, şema, rubrik ve doküman şablonları.

## Hızlı başlangıç

Depoyu klonlayın; varsayılan `core-development` paketini kurun:

```bash
git clone https://github.com/egeetas/skills.git "$HOME/.local/share/egeetas-skills"
cd "$HOME/.local/share/egeetas-skills"
./scripts/install.sh
```

Paket, tekil skill veya tüm koleksiyon kurulabilir:

```bash
./scripts/install.sh --list-packs
./scripts/install.sh --pack product-architecture --pack frontend-mobile
./scripts/install.sh code-review test-and-fix-loop
./scripts/install.sh --all --with-agents
```

Veya Codex'e şunu söyleyin:

```text
Use $skill-installer to install skills from https://github.com/egeetas/skills
```

Plugin, kullanıcı ve repository kapsamlı yöntemler için [SETUP.tr.md](SETUP.tr.md) dosyasına bakın.

## Skill paketleri

| Paket | Skill | Amaç |
| --- | ---: | --- |
| `core-development` | 17 | Uygulama, test, review, git, issue, PR ve release |
| `product-architecture` | 7 | Ürün doğrulama, gereksinim, mimari, API ve başlangıç |
| `frontend-mobile` | 9 | Tasarım, tarayıcı kalitesi, erişilebilirlik, görsel kontrol ve mobil teslim |
| `security-operations` | 7 | Güvenlik, migration, observability, performans ve incident |
| `project-intelligence` | 3 | Kalıcı öğrenimler, oturum devri ve retrospektif |
| `ai-documentation` | 6 | MCP, AI eval/güvenlik, prompt ve teknik dokümantasyon |

Her skill yalnızca bir pakette bulunur. Tam [katalog](CATALOG.md), skill'lerin görevini ve en yakın sınırını açıklar.

## Kullanım

Codex'te `/skills` komutunu kullanın veya skill'i açıkça çağırın:

```text
$product-strategy-review bu fikrin talep kanıtını sorgula
$codebase-mapping değiştirmeden önce ödeme akışını haritala
$test-and-fix-loop ilgili kontrolleri çalıştır ve doğrulanmış hataları düzelt
$issue-to-pr-workflow 42 numaralı issue'yu doğrulanmış bir PR olarak teslim et
```

`software-development-workflow` bilerek yalnızca açık çağrıyla çalışır; birden çok yaşam döngüsü aşamasını koordine etmek istediğinizde kullanın. Odaklı skill'ler görev açıklamaları eşleştiğinde otomatik seçilebilir.

## Repo yapısı

```text
skills/<name>/             Skill talimatları ve isteğe bağlı kaynaklar
packs/                     Hazır kurulum seçimleri
agent-presets/             İsteğe bağlı Codex subagent'ları
scripts/                   Kurucu, doğrulayıcı ve routing eval aracı
tests/                     Sınır ve tam routing corpus'ları
templates/                 Yeni skill şablonu
plugin.json                Taşınabilir plugin manifesti
.codex-plugin/plugin.json  Uyumluluk manifesti
.agents/plugins/           Marketplace metadata'sı
```

## Geliştirme

```bash
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/run_routing_evals.py --dry-run
```

Geliştirme araçları Python 3.11 veya üzerini gerektirir; seçilen bir skill kendi yardımcı script'ini çalıştırmadıkça skill kullanımı Python gerektirmez.

Gerçek model kullanan routing eval aracı yapılandırılmış Codex hesabınızı kullanır ve kullanım kotası tüketebilir:

```bash
python3 scripts/run_routing_evals.py --limit 12 --output routing-report.json
```

Katkı öncesinde [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını okuyun. [Skill yazım rehberi](docs/skill-authoring.md), `SKILL.md`, `agents/openai.yaml`, script, reference, asset, paket ve eval yapılarının birlikte nasıl çalıştığını anlatır.

## Lisans ve atıf

Özgün içerik [MIT](LICENSE) lisanslıdır. Uyarlanan materyaller kaynak lisanslarını korur; [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) ve [`LICENSES/`](LICENSES/) dizinine bakın.

Resmî kaynaklar: [Codex skills](https://developers.openai.com/codex/skills) · [Codex plugins](https://developers.openai.com/codex/plugins/build)
