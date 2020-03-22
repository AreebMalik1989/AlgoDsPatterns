# MVC design pattern implementation in Java8

### Some points to mention

* The model knows nothing about the view or the controller. The view knows nothing about the model or the controller. The controller understands both the model and the view.
* The model uses observables, essentially when important data is changed, any interested listener get notified through a callback mechanism.
* The cool thin is anything modifying the model will notify the controller. In this case it is controller modifying the model, but it could be anything else, even another controller off in the distance looking at something else.
* The main idea is that you give a controller the model and view that it needs, but model's can be shared between controllers so that when model is updated, all associated views are updated. -Brian Kelley