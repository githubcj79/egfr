# Taken from https://micropyramid.com/blog/how-to-use-nested-formsets-in-django/

# models.py

class Parent(models.Model):
    name = models.CharField(max_length=255)

class Child(models.Model):
    parent = models.ForeignKey(Parent)
    name = models.CharField(max_length=255)

class Address(models.Model):
    child = models.ForeignKey(Child)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

# forms.py - cada formset en una página

from django.forms.models import inlineformset_factory

ChildrenFormset = inlineformset_factory(models.Parent, models.Child, extra=1)
AddressFormset = inlineformset_factory(models.Child, models.Address, extra=1)

# forms.py - formsets anidados

from django.forms.models import BaseInlineFormSet

class BaseChildrenFormset(BaseInlineFormSet):

    def save(self, commit=True):

        result = super(BaseChildrenFormset, self).save(commit=commit)

        for form in self.forms:
            if hasattr(form, 'nested'):
                if not self._should_delete_form(form):
                    form.nested.save(commit=commit)

        return result

    def is_valid(self):
            result = super(BaseChildrenFormset, self).is_valid()

            if self.is_bound:
                for form in self.forms:
                    if hasattr(form, 'nested'):
                        result = result and form.nested.is_valid()

            return result

    def add_fields(self, form, index):
        super(BaseChildrenFormset, self).add_fields(form, index)

        # save the formset in the 'nested' property
        form.nested = AddressFormset(
                        instance=form.instance,
                        data=form.data if form.is_bound else None,
                        files=form.files if form.is_bound else None,
                        prefix='address-%s-%s' % (
                            form.prefix,
                            AddressFormset.get_default_prefix()),
                        extra=1)

ChildrenFormset = inlineformset_factory(models.Parent,
                                        models.Child,
                                        formset=BaseChildrenFormset,
                                        extra=1)

