# -*- coding: utf-8 -*-
from django.db import models
import uuid

class UUIDField(models.CharField) :
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 64)
        kwargs['blank'] = True
        models.CharField.__init__(self, *args, **kwargs)

    def pre_save(self, model_instance, add):
        if add :
            if hasattr(model_instance, self.attname) and getattr(model_instance, self.attname) != None: 
                attr_val = getattr(model_instance, self.attname)
                if attr_val != None and len(attr_val.strip()) > 0:
                    return getattr(model_instance, self.attname)       
            
            value = str(uuid.uuid4())
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(models.CharField, self).pre_save(model_instance, add)