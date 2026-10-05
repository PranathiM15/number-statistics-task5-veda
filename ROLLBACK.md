# Rollback Evidence

If a future change breaks the project, Git can restore the previous committed version.

## View commits

```powershell
git log --oneline
```

## Safest rollback approach

Create a branch from the last known-good commit:

```powershell
git switch -c recovery
```

If the latest commit itself needs to be undone while preserving history:

```powershell
git revert HEAD
git push
```

Do not delete the repository to recover from a mistake. Git history provides the rollback trail.

## Submission evidence

The first successful submission commit is:

```text
Complete Task 5 Number Statistics web application
```

Additional fixes should use clear commit messages, for example:

```text
Fix input validation
Improve responsive layout
Fix even odd classification
```
