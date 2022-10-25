from abc import ABC, abstractmethod


class AbcWorker(ABC):
    @abstractmethod
    def work(self):
        pass


class Worker(AbcWorker):
    def work(self):
        print("I'm working!!")


class WorkerValidator:
    @staticmethod
    def validate_worker(worker):
        assert isinstance(worker, AbcWorker), '`worker` must be of type {}'.format(Worker)


class Manager:
    def __init__(self, validator):
        self.validator = validator
        self.worker = None

    def set_worker(self, worker):
        self.validator.validate_worker(worker)
        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


class SuperWorker(AbcWorker):
    def work(self):
        print("I work very hard!!!")


class LazyWorker(AbcWorker):
    def work(self):
        print("I'm sleeping...")


worker = Worker()
validator = WorkerValidator()
manager = Manager(validator)
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
except AssertionError:
    print("manager fails to support super_worker....")
manager.manage()
lazy_worker = LazyWorker()
manager_2 = Manager(validator)
try:
    manager_2.set_worker(lazy_worker)
except AssertionError:
    print("manager fails to support lazy_worker....")
manager_2.manage()