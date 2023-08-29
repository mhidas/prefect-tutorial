# prefect-tutorial
Learning &amp; exploring how Prefect works. Following the tutorial [here](https://docs.prefect.io/2.11.4/tutorial/)

## Notes

### Flows
* Python function with `@flow` decorator
* Can have inputs and output
* Has state
* Can validate input types
* Retries & timeouts

### Tasks
* Python function with `@task` decorator
* _Must be called from within a flow_
* Atomic piece of work, executed independently
* Can run concurrently
* Return value can be cached in between runs (locally, not on Cloud)
* Retries & timeouts

### Deployments
Up to here: https://docs.prefect.io/2.11.5/tutorial/deployments/
