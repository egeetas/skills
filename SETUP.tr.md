# Kurulum

[English](SETUP.md)

Kurucu Bash gerektirir. Repo doğrulama ve yardımcı script'ler Python 3.11 veya üzerini gerektirir.

## Codex plugin olarak kurulum

Depoda güncel Codex plugin araçlarının beklediği taşınabilir `plugin.json`, uyumluluk için `.codex-plugin/plugin.json` ve marketplace metadata'sı vardır.

```bash
codex plugin marketplace add egeetas/skills --ref v1.0.0
codex plugin add codex-engineering-skills@egeetas-skills
```

Yeni skill'ler görünmezse Codex'i yeniden başlatın. `/skills` komutunu veya `$` ile açılan skill seçiciyi kullanın.

## Repo script'i ile kurulum

Depoyu kalıcı bir konuma klonlayın:

```bash
git clone https://github.com/egeetas/skills.git "$HOME/.local/share/egeetas-skills"
cd "$HOME/.local/share/egeetas-skills"
```

Varsayılan komut 17 skill içeren `core-development` paketini `$HOME/.agents/skills` altına symlink eder:

```bash
./scripts/install.sh
```

İçeriği keşfedin ve seçin:

```bash
./scripts/install.sh --list
./scripts/install.sh --list-packs
./scripts/install.sh --pack frontend-mobile --pack security-operations
./scripts/install.sh product-strategy-review codebase-mapping
./scripts/install.sh --all
```

İsteğe bağlı `code-explorer`, `quality-reviewer` ve `test-investigator` preset'lerini `$HOME/.codex/agents` altına ekleyin:

```bash
./scripts/install.sh --all --with-agents
```

Kurucu mevcut bir dosya, klasör veya ilgisiz symlink üzerine yazmaz.

## Repository kapsamlı kurulum

Seçilen içeriği projenin `.agents/skills` dizinine kopyalayın:

```bash
./scripts/install.sh --scope repo --target /absolute/path/to/project --pack core-development
```

Preset'leri `<project>/.codex/agents` altına kopyalamak için `--with-agents` ekleyin. Repository kapsamı kopya kullandığından sonraki upstream değişiklikleri otomatik gelmez; yeni sürümü diff olarak inceleyin.

## Güncelleme ve doğrulama

```bash
git -C "$HOME/.local/share/egeetas-skills" pull --ff-only
python3 "$HOME/.local/share/egeetas-skills/scripts/validate_skills.py"
```

Kullanıcı kapsamındaki symlink'ler güncel checkout'u hemen kullanır. Kurucu mevcut repository kopyalarını bilerek güncellemez. Kaynak ve hedefi karşılaştırın; yalnızca değiştirmeyi onayladığınız skill dizinlerini taşıyın veya kaldırın, ardından aynı kurulum komutunu yeniden çalıştırın.

## Sorun giderme

- Aynı ada sahip skill'ler birleştirilmez; eski veya çakışan kopyayı kaldırın.
- Conflict mesajı, kurucunun mevcut hedefi bilerek koruduğu anlamına gelir.
- Codex'i repository'nin `.agents/skills` dizimini kapsayan bir çalışma yolunda başlatın.
- Metadata ile keşif sorununu ayırmak için `python3 scripts/validate_skills.py` çalıştırın.

Resmî dokümantasyon: [Codex skills](https://developers.openai.com/codex/skills) · [Codex plugins](https://developers.openai.com/codex/plugins/build)
