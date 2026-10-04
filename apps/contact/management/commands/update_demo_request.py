from apps.contact.models import DemoRequest

records = list(DemoRequest.objects.all())

for record in records:
    record.status = DemoRequest.Status.CONTACTED

DemoRequest.objects.bulk_update(
    records,
    ["status"],
    batch_size=500
)