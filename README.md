# Managing Conda Environments

This document provides a comprehensive guide to saving, sharing, creating, and managing Conda environments effectively.

## Overview
Conda environments are powerful tools for managing dependencies and ensuring reproducibility in projects. By saving and sharing your environment configurations, you can ensure that others use the exact package versions you used, reducing compatibility issues.

---

## Exporting an Environment
To list all package names and their versions in the current environment, run:

```bash
conda env export
```

The output displays the name of the environment and all its dependencies. You can save this information to a YAML file:

```bash
conda env export > environment.yaml
```

### Key Points:
- The `environment.yaml` file will be created (or overwritten) in the current directory.
- Share this file via GitHub or other means so others can recreate your environment.

---

## Creating an Environment from a File
To recreate an environment using an `environment.yaml` file, use:

```bash
conda env create -f environment.yaml
```

This will create a new environment with the name specified in the `environment.yaml` file.

---

## Listing Environments
If you forget the names of your environments, list them with:

```bash
conda env list
```

or:

```bash
conda info --envs
```

The current active environment will have an asterisk (`*`) next to its name. The default environment is named `base`.

---

## Viewing Installed Packages
To view all installed packages in an environment:

- If the environment is **not activated**:

```bash
conda list -n env_name
```

- If the environment **is activated**:

```bash
conda list
```

- To check if a specific package (e.g., `scipy`) is installed:

```bash
conda list -n env_name scipy
```

---

## Removing an Environment
To delete an environment that is no longer needed, run:

```bash
conda env remove -n env_name
```

Replace `env_name` with the name of the environment you want to remove.

---

## Notes
- Always double-check the name of the environment before deleting.
- Use version control platforms like GitHub to share the `environment.yaml` file for better collaboration.

---

## Additional Resources
- [Conda Documentation](https://docs.conda.io/)
- [YAML File Format](https://yaml.org/)

---

This guide was developed as part of the Udacity and Accenture initiative to enhance environment management skills.

