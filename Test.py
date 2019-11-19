from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import inspect
from sqlalchemy import Integer
from sqlalchemy import or_
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy.orm import with_polymorphic


Base = declarative_base()


class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    employees = relationship(
        "Person", back_populates="company", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return "Company %s" % self.name


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    company_id = Column(ForeignKey("company.id"))
    name = Column(String(50))
    type = Column(String(50))

    company = relationship("Company", back_populates="employees")

    __mapper_args__ = {
        "polymorphic_identity": "person",
        "polymorphic_on": type,
    }

    def __repr__(self):
        return "Ordinary person %s" % self.name


class Engineer(Person):
    __tablename__ = "engineer"
    id = Column(ForeignKey("person.id"), primary_key=True)
    status = Column(String(30))
    engineer_name = Column(String(30))
    primary_language = Column(String(30))

    __mapper_args__ = {"polymorphic_identity": "engineer"}

    def fun(self):
        print("Selamun Aleyküm-----------")

    def __repr__(self):
        return (
            "Engineer %s, status %s, engineer_name %s, "
            "primary_language %s"
            % (
                self.name,
                self.status,
                self.engineer_name,
                self.primary_language,
            )
        )


class Manager(Person):
    __tablename__ = "manager"
    id = Column(ForeignKey("person.id"), primary_key=True)
    status = Column(String(30))
    manager_name = Column(String(30))

    __mapper_args__ = {"polymorphic_identity": "manager"}

    def __repr__(self):
        return "Manager %s, status %s, manager_name %s" % (
            self.name,
            self.status,
            self.manager_name,
        )


engine = create_engine("sqlite://", echo=True)
Base.metadata.create_all(engine)

session = Session(engine)

c = Company(
    name="company1",
    employees=[
        Manager(
            name="pointy haired boss", status="AAB", manager_name="manager1"
        ),
        Engineer(
            name="dilbert",
            status="BBA123536528",
            engineer_name="engineer1",
            primary_language="java",
        ),
        Person(name="joesmith"),
        Engineer(
            name="wally",
            status="CGG",
            engineer_name="engineer2",
            primary_language="python",
        ),
        Manager(name="jsmith", status="ABA", manager_name="manager2"),
    ],
)
session.add(c)

session.commit()


dilbert = session.query(Person).filter_by(name="dilbert").one()
print(isinstance(dilbert,Person))
#dilbert2 = session.query(Engineer).filter_by(name="dilbert").one()
#assert dilbert is dilbert2
dilbert.fun()
print(dilbert.type)


# query using with_polymorphic.

'''
eng_manager = with_polymorphic(Person, [Engineer, Manager])
print(
    type(session.query(eng_manager)
    .filter(
        or_(
            eng_manager.Engineer.engineer_name == "engineer1",
            eng_manager.Manager.manager_name == "manager2",
        )
    )
    .all()[0])
)

# illustrate join from Company.
# flat=True means the tables inside the "polymorphic join" will be aliased.
# not strictly necessary in this example but helpful for the more general
# case of joins involving inheritance hierarchies as well as joined eager
# loading.
'''