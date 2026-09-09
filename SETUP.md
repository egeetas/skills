# Codex Skill Setup / Codex Skill Kurulumu

[Türkçe](#türkçe) · [English](#english)

## Türkçe

Codex skill'leri kullanıcı kapsamından veya belirli bir repository kapsamından yükler:

- Kullanıcı kapsamı: `$HOME/.agents/skills`
- Repository kapsamı: `<repo>/.agents/skills`

### Yöntem 1 — Codex skill-installer

Codex'e şu isteği verin:

```text
Use $skill-installer to install skills from https://github.com/egeetas/skills
```

Belirli skill'ler için isimleri isteğe ekleyin:

```text
Use $skill-installer to install frontend-design, webapp-testing, and test-and-fix-loop from https://github.com/egeetas/skills
```

### Yöntem 2 — Kişisel kurulum

Bu yöntem depoyu kalıcı bir klasöre klonlar ve skill klasörlerini resmi kullanıcı konumuna symlink eder. Böylece `git pull` sonrasında skill'ler ayrıca kopyalanmadan güncellenir.

```bash
git clone https://github.com/egeetas/skills.git "$HOME/.local/share/egeetas-skills"
cd "$HOME/.local/share/egeetas-skills"
./scripts/install.sh
```

Mevcut skill listesini görmek için:

```bash
./scripts/install.sh --list
```

Yalnızca belirli skill'leri kurmak için:

```bash
./scripts/install.sh frontend-design webapp-testing mcp-builder
```

Farklı bir kullanıcı skill klasörü seçmek için:

```bash
./scripts/install.sh --target /absolute/path/to/skills
```

Kurulum script'i var olan dosya veya symlink'lerin üzerine yazmaz; çakışmaları raporlayarak durur.

### Yöntem 3 — Repository kapsamlı kurulum

Bir projeyle birlikte versiyonlanacak skill'leri `<proje>/.agents/skills` altına kopyalayın:

```bash
cd "$HOME/.local/share/egeetas-skills"
./scripts/install.sh --scope repo --target /absolute/path/to/project
```

Seçili kurulum:

```bash
./scripts/install.sh --scope repo --target /absolute/path/to/project \
  code-review testing-standards test-and-fix-loop
```

Repository kapsamı kopyalama kullandığı için güncellemeler otomatik gelmez; yeni sürümü kontrollü bir diff ile tekrar taşıyın.

### Doğrulama

Codex CLI veya IDE extension içinde:

1. `/skills` komutunu çalıştırın veya `$` yazarak skill seçiciyi açın.
2. Örneğin `$frontend-design` veya `$test-and-fix-loop` çağırın.
3. Yeni skill görünmezse Codex'i yeniden başlatın.

Depo yapısını doğrulamak için:

```bash
python3 scripts/validate_skills.py
```

### Güncelleme

```bash
git -C "$HOME/.local/share/egeetas-skills" pull --ff-only
python3 "$HOME/.local/share/egeetas-skills/scripts/validate_skills.py"
```

Kişisel kurulum symlink kullandığı için başarılı pull sonrasında yeni içerik doğrudan kullanılabilir.

### Sorun giderme

- Aynı `name` değerine sahip iki skill varsa Codex bunları birleştirmez; ikisi de listede görünebilir. Eski veya çakışan kopyayı kaldırın.
- Script bir hedefi üzerine yazmaz. Önce mevcut skill'i inceleyin; gerçekten kaldırmak istiyorsanız yalnızca doğruladığınız symlink veya klasörü hedefleyin.
- Repository içinden Codex başlatırken, `.agents/skills` klasörünün çalışma dizini ile repo kökü arasındaki yol üzerinde olduğundan emin olun.

## English

Codex discovers skills from user and repository scopes:

- User scope: `$HOME/.agents/skills`
- Repository scope: `<repo>/.agents/skills`

### Option 1 — Codex skill-installer

Ask Codex:

```text
Use $skill-installer to install skills from https://github.com/egeetas/skills
```

For a subset:

```text
Use $skill-installer to install frontend-design, webapp-testing, and test-and-fix-loop from https://github.com/egeetas/skills
```

### Option 2 — User-level installation

Clone the repository into a stable location and symlink its skill directories into the official user scope:

```bash
git clone https://github.com/egeetas/skills.git "$HOME/.local/share/egeetas-skills"
cd "$HOME/.local/share/egeetas-skills"
./scripts/install.sh
```

List or install selected skills:

```bash
./scripts/install.sh --list
./scripts/install.sh frontend-design webapp-testing mcp-builder
```

Use a custom user destination:

```bash
./scripts/install.sh --target /absolute/path/to/skills
```

The installer never overwrites an existing file, directory, or different symlink.

### Option 3 — Repository-scoped installation

Copy all skills into a project's `.agents/skills` directory:

```bash
cd "$HOME/.local/share/egeetas-skills"
./scripts/install.sh --scope repo --target /absolute/path/to/project
```

Copy a selected set:

```bash
./scripts/install.sh --scope repo --target /absolute/path/to/project \
  code-review testing-standards test-and-fix-loop
```

Repository scope uses copies so the skills can be committed with the target project. Updates are not automatic; review and copy future versions as an explicit diff.

### Verify

1. Run `/skills` in Codex CLI or the IDE extension, or type `$` to open the skill selector.
2. Invoke a skill such as `$frontend-design` or `$test-and-fix-loop`.
3. Restart Codex if a newly installed skill does not appear.

Validate this repository:

```bash
python3 scripts/validate_skills.py
```

### Update

```bash
git -C "$HOME/.local/share/egeetas-skills" pull --ff-only
python3 "$HOME/.local/share/egeetas-skills/scripts/validate_skills.py"
```

User-level symlinks immediately expose the successfully pulled version.

### Troubleshooting

- Codex does not merge duplicate skill names. Remove or disable stale duplicate copies.
- The installer refuses to overwrite conflicts. Inspect the existing destination before removing anything.
- For repository skills, start Codex within a directory whose path to the repository root includes `.agents/skills`.

Official documentation: <https://developers.openai.com/codex/skills>
