from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        res = ""
        for sub in self.subscriptions:
            if sub.id == subscription_id:
                res += str(sub) + "\n"
        for cust in self.customers:
            if cust.id == subscription_id:
                res += str(cust) + "\n"
        for tr in self.trainers:
            if tr.id == subscription_id:
                res += str(tr) + "\n"
        for equip in self.equipment:
            if equip.id == subscription_id:
                res += str(equip) + "\n"
        for pl in self.plans:
            if pl.id == subscription_id:
                res += str(pl) + "\n"
        return res.strip()
