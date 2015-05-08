# Dependencies
import pyblish_endpoint.service

import hdefereval

wrapper = hdefereval.executeInMainThreadWithResult


class HoudiniService(pyblish_endpoint.service.EndpointService):
    def init(self, *args, **kwargs):
        orig = super(HoudiniService, self).init
        return wrapper(orig, *args, **kwargs)

    def process(self, *args, **kwargs):
        orig = super(HoudiniService, self).process
        return wrapper(orig, *args, **kwargs)

    def repair(self, *args, **kwargs):
        orig = super(HoudiniService, self).repair
        return wrapper(orig, *args, **kwargs)
