import pandas as pd

from django.core.management.base import BaseCommand

from apps.organizations.models import (
    SchoolBoardWithdrawal
)


class Command(BaseCommand):

    help = (
        "Import School Board Withdrawals"
    )

    def add_arguments(
        self,
        parser
    ):

        parser.add_argument(
            "csv_file",
            type=str
        )

    def handle(
        self,
        *args,
        **options
    ):

        data = pd.read_csv(
            options["csv_file"]
        )

        withdrawals = []

        batch_size = 1000

        total = 0

        for _, row in data.iterrows():

            withdrawals.append(

                SchoolBoardWithdrawal(

                    registration_id=int(
                        row[
                            "registration_id"
                        ]
                    ),

                    withdrawal_date=row[
                        "withdrawal_date"
                    ],

                    reason_type=row[
                        "reason_type"
                    ],

                    reason=row[
                        "reason"
                    ],

                    remarks=row[
                        "remarks"
                    ]
                )
            )

            if len(withdrawals) >= batch_size:

                SchoolBoardWithdrawal.objects.bulk_create(
                    withdrawals,
                    batch_size=batch_size,
                    ignore_conflicts=True
                )

                total += len(
                    withdrawals
                )

                print(
                    f"{total} imported"
                )

                withdrawals = []

        if withdrawals:

            SchoolBoardWithdrawal.objects.bulk_create(
                withdrawals,
                batch_size=batch_size,
                ignore_conflicts=True
            )

            total += len(
                withdrawals
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"{total} withdrawals imported"
            )
        )