#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/18 13:35
'''
条件变量总是与某种锁相关联; 这可以传入，或者默认情况下会创建一个。当多个条件变量必须共享同一个锁时，传入一个很有用。锁是条件对象的一部分：您不必单独跟踪它。

条件变量服从上下文管理协议：使用该with语句在封闭块的持续时间内获取关联的锁。该acquire()和 release()方法也调用相关的锁的相应方法。

必须在保持关联锁的情况下调用其他方法。该 wait()方法释放锁，然后阻塞，直到另一个线程通过调用notify()或 唤醒它notify_all()。一旦被唤醒，wait() 重新获得锁并返回。也可以指定超时。

该notify()方法唤醒等待条件变量的其中一个线程（如果有的话）正在等待。该notify_all() 方法唤醒等待条件变量的所有线程。

注意：notify()和notify_all()方法不释放锁; 这意味着被唤醒的一个或多个线程不会wait()立即从它们的调用中返回，而是仅在调用notify()或notify_all() 最终放弃锁的所有权的线程中。

使用条件变量的典型编程风格使用锁来同步对某些共享状态的访问; 对状态的特定变化感兴趣的线程wait()重复调用，直到它们看到所需的状态，而线程修改状态调用 notify()或者notify_all()当它们改变状态时，它可能是其中一个服务员的期望状态。例如，以下代码是具有无限缓冲区容量的通用生产者 - 消费者情况：

# Consume one item
with cv:
    while not an_item_is_available():
        cv.wait()
    get_an_available_item()

# Produce one item
with cv:
    make_an_item_available()
    cv.notify()


该while循环检查应用程序的条件是必要的，因为wait()可以任意长的时间后返回，并促使病情notify()通话可能不再成立。这是多线程编程所固有的。该 wait_for()方法可用于自动化条件检查，并简化超时计算：

# Consume an item
with cv:
    cv.wait_for(an_item_is_available)
    get_an_available_item()
要在notify()和之间进行选择notify_all()，请考虑一个状态更改是否只对一个或多个等待线程感兴趣。例如，在典型的生产者 - 消费者情况下，向缓冲区添加一个项目只需要唤醒一个消费者线程。

class threading.Condition（lock = None ）
此类实现条件变量对象。条件变量允许一个或多个线程等待，直到另一个线程通知它们。

如果给定了lock参数None，则它必须是一个Lock 或RLock对象，并且它被用作底层锁。否则，将RLock创建一个新对象并将其用作基础锁。

在版本3.3中更改：从工厂功能更改为类。

acquire（* args ）
获取底层锁。此方法在底层锁上调用相应的方法; 返回值是该方法返回的任何值。

release（）
释放底层锁。此方法在底层锁上调用相应的方法; 没有回报价值。

wait（超时=无）
等到通知或直到发生超时。如果在调用此方法时调用线程尚未获取锁定，RuntimeError则引发a。

此方法释放底层锁，然后阻塞，直到它被另一个线程中的相同条件变量唤醒notify()或notify_all()调用，或者直到发生可选超时。一旦被唤醒或超时，它就会重新获得锁定并返回。

当超时参数存在而不存在时None，它应该是一个浮点数，指定操作的超时（以秒为单位）（或其分数）。

当底层锁是a时RLock，它不会使用其release()方法释放，因为当递归多次获取时，这实际上可能无法解锁。相反，使用了RLock类的内部接口，即使多次递归获取它也能真正解锁它。然后，在重新获取锁时，使用另一个内部接口来恢复递归级别。

返回值是True除非给定的超时到期，在这种情况下它是False。

版本3.2中已更改：以前，该方法始终返回None。

wait_for（谓词，超时=无）
等到条件评估为真。 谓词应该是可调用的，结果将被解释为布尔值。一个超时可以提供给最长等待时间。

此实用程序方法可以wait()重复调用，直到满足谓词，或者直到超时发生。返回值是谓词的最后一个返回值，并将评估 False方法是否超时。

忽略超时功能，调用此方法大致相当于编写：

while not predicate():
    cv.wait()
因此，相同的规则适用于wait()：锁定必须在被调用时保持并在返回时重新获取。使用锁定评估谓词。

版本3.2中的新功能。

notify（n = 1 ）
默认情况下，唤醒一个等待此条件的线程（如果有）。如果在调用此方法时调用线程尚未获取锁定， RuntimeError则引发a。

此方法最多唤醒等待条件变量的n个线程; 如果没有线程在等待，那么这是一个无操作。

如果至少有n个 线程在等待，那么当前的实现正好会唤醒n 个线程。但是，依赖这种行为是不安全的。未来的优化实现有时可能会唤醒超过 n个线程。

注意：唤醒线程实际上不会从其wait() 调用返回，直到它可以重新获取锁定。由于notify()不释放锁，其调用者应该。

notify_all（）
唤醒等待这种情况的所有线程。此方法就像 notify()，但唤醒所有等待的线程而不是一个。如果在调用此方法时调用线程尚未获取锁定， RuntimeError则引发a。
'''
