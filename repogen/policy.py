"""Submission rules specific to the Native-Webos catalog."""


def require_native_type(metadata: dict, source: str) -> None:
    if metadata.get('type') != 'native':
        raise ValueError(f'{source}: only native webOS applications (type: native) are accepted; '
                         'web applications and web wrappers are not eligible.')
