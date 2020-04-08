"""
Proxy design pattern implementation

Intent:

    Proxy is a structural design pattern that lets you provide a substitute or
    placeholder for another object. A proxy controls access to the original
    object, allowing you to perform something either before or after the
    request gets through to the original object.

Structure:

1.  Service Interface: declares the interface of the Service. The proxy must
    follow this interface to be able to disguise itself as a service object.

2.  Service: is a class that provides some useful business logic.

3.  Proxy class: has a reference field that points to a service object. After
    the proxy finishes its processing (e.g., lazy initialization, logging,
    access control, caching, etc.), it passes the request to the service
    object.

4.  Client: should work with both services and proxies via the same interface.
    This way you can pass a proxy into any code that expects a service object.
"""


from abc import ABC, abstractmethod


class Subject(ABC):
    """
    The Subject interface declares common operations for both RealSubject and
    the Proxy. As long as the Client works with RealSubject using this
    interface, you'll be able to pass it a proxy instead of the real subject.
    """
    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):
    """
    The RealSubject contains some core business logic. Usually, RealSubjects
    are capable of doing some useful work which may also be very slow or
    sensitive - e.g., correcting input data. A Proxy can solve these issues
    without any changes to the RealSubject's code.
    """
    def request(self) -> None:
        print("RealSubject: Handling request.")


class Proxy(Subject):
    """
    The proxy has an interface identical to RealSubject.
    """
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        """
        The most common application of the Proxy pattern are lazy loading,
        caching, controlling the access, logging, etc. A Proxy can perform one
        of these things and then, depending on result, pass the execution to
        the same method in a linked RealSubject object.
        """
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request")


def client_code(subject: Subject) -> None:
    """
    The client code is supposed to work with all objects (both subjects and
    proxies) via the Subject interface in order to support both real subjects
    and proxies. In real life, however, clients mostly work with their real
    subjects directly. In this case, to implement the pattern more easily, you
    can extend your proxy from the real subject's class.
    """

    # ...
    subject.request()
    # ...


if __name__ == "__main__":
    
    print("Client: Executing the client code with real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)
