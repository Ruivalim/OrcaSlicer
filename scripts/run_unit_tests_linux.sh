#!/usr/bin/env bash
set -e

# Runs the unit test suite inside the same Linux builder container that
# build_linux.sh -g uses. Tests bake absolute /__w/OrcaSlicer/OrcaSlicer data
# paths in at compile time (TEST_DATA_DIR/PROFILES_DIR), so they only find
# their fixtures with the repo mounted at that path.
#
# Usage: ./scripts/run_unit_tests_linux.sh [extra ctest args]

SCRIPT_PATH=$(dirname "$(readlink -f "${0}")")/..
cd "${SCRIPT_PATH}"

# Same image tag recipe as get_docker_runner_image in build_linux.sh.
container_cli="${ORCA_CONTAINER_CLI:-docker}"
base_image="${ORCA_DOCKER_BASE_IMAGE:-ubuntu:24.04}"
docker_cmake_version="${ORCA_DOCKER_CMAKE_VERSION-4.3.0}"
recipe_hash=$(find "${SCRIPT_PATH}/build_linux.sh" "${SCRIPT_PATH}/scripts/linux.d" -type f -print0 | sort -z | xargs -0 cat | sha256sum | cut -c1-12)
sanitized_base_image=$(echo "${base_image}" | tr '/:@' '---' | tr -cs 'A-Za-z0-9_.-' '-')
sanitized_cmake_version=$(echo "${docker_cmake_version:-system}" | tr -cs 'A-Za-z0-9_.-' '-')
image="${ORCA_DOCKER_IMAGE:-orcaslicer-linux-builder:${sanitized_base_image}-cmake-${sanitized_cmake_version}-${recipe_hash}}"

exec "${container_cli}" run --rm -i \
    -u "$(id -u):$(id -g)" -e HOME=/tmp \
    -v "${SCRIPT_PATH}:/__w/OrcaSlicer/OrcaSlicer" \
    -w /__w/OrcaSlicer/OrcaSlicer \
    "${image}" \
    ./scripts/run_unit_tests.sh build/tests Release "$@"
