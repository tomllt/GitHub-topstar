<h1>
  <img alt="Containerization logo" src="./assets/Containerization-Logo.png" width="70" valign="middle">
  &nbsp;container
</h1>

`container` is a tool that you can use to create and run Linux containers as lightweight virtual machines on your Mac. It's written in Swift, and optimized for Apple silicon.

The tool consumes and produces [OCI-compatible container images](https://github.com/opencontainers/image-spec), so you can pull and run images from any standard container registry. You can push images that you build to those registries as well, and run the images in any other OCI-compatible application.

`container` uses the [Containerization](https://github.com/apple/containerization) Swift package for low-level container, image, and process management.

![introductory movie showing some basic commands](./docs/assets/landing-movie.gif)

## Get started

### Requirements

You need a Mac with Apple silicon to run `container`. To build it, see the [BUILDING](./BUILDING.md) document.

`container` is supported on macOS 26, since it takes advantage of new features and enhancements to virtualization and networking in this release. We do not support older versions of macOS and the `container` maintainers typically will not address issues that cannot be reproduced on macOS 26.

### Initial install

Download the latest signed installer package for `container` from the [GitHub release page](https://github.com/apple/container/releases).

To install the tool, double-click the package file and follow the instructions. Enter your administrator password when prompted, to give the installer permission to place the installed files under `/usr/local`.

Start the system service with:

```bash
container system start
```

### Upgrade or downgrade

For both upgrading and downgrading, you can manually download and install the signed installer package by following the steps from [initial install](#initial-install) or use the `update-container.sh` script (installed to `/usr/local/bin`).


... (truncated)