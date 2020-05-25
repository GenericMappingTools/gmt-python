---
name: PyGMT release checklist
about: Checklist for a new PyGMT release.
title: 'Release PyGMT x.x.x'
labels: 'maintenance'
assignees: ''

---

**Release**: [v0.x.x](https://github.com/GenericMappingTools/pygmt/milestones/0.x.x)
**Scheduled Date**: YYYY/MM/DD

**Before release**:
- [ ] Reserve a DOI on [Zenodo](https://zenodo.org) by clicking on "New Version"
- [ ] Update Changelog

**Release**:
- [ ] Make a tag and push it to Github
```
git tag vX.Y.Z
git push --tags
```
- [ ] Go to [GitHub Release](https://github.com/GenericMappingTools/pygmt/releases) and make a release
- [ ] Manually upload the pygmt-vX.Y.Z.zip file to https://zenodo.org/deposit, make sure you file it under the correct reserved DOI
- [ ] Announce the releases on the GMT [forum](https://forum.generic-mapping-tools.org/c/news/), [website](https://github.com/GenericMappingTools/website) (News) and [ResearchGate](https://www.researchgate.net/project/PyGMT-A-Python-interface-for-the-Generic-Mapping-Tools)

**After release**:
- [ ] Create branch 0.x for bug-fixes if this is a minor release (i.e. create branch 0.1 after 0.1.0 is released)
- [ ] Commit changes to Github

**3rd party update**:
- [ ] Update conda-forge [pygmt-feedstock](https://github.com/conda-forge/pygmt-feedstock) [Usually done automatically by conda-forge's bot]

---

- [ ] Party :tada: (don't tick before all other checkboxes are ticked!)
