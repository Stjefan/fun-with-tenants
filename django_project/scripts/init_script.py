from dauerauswertung.models import Client, Domain

def run():
    if False:
        tenant = Client(schema_name='public',
                        name='Schemas Inc.',
                        )
        tenant.save()

        # Add one or more domains for the tenant
        domain = Domain()
        domain.domain = 'localhost' # don't add your port or www here! on a local server you'll want to use localhost here
        domain.tenant = tenant
        domain.is_primary = True
        domain.save()


        # create your first real tenant
        tenant = Client(schema_name='tenant1',
                        name='Fonzy Tenant',
                        )
        tenant.save() # migrate_schemas automatically called, your tenant is ready to be used!

        # Add one or more domains for the tenant
        domain = Domain()
        domain.domain = 'go' # don't add your port or www here!
        domain.tenant = tenant
        domain.is_primary = True
        domain.save()

    tenant = Client(schema_name='tenant 2',
                    name='Immendingen',
                    )
    tenant.save() # migrate_schemas automatically called, your tenant is ready to be used!

    # Add one or more domains for the tenant
    domain = Domain()
    domain.domain = 'leave' # don't add your port or www here!
    domain.tenant = tenant
    domain.is_primary = True
    domain.save()
