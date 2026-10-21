Early submission bonus example
==============================

This mock module demonstrates the early submission bonus configuration.
Its early cutoff matches the normal deadline used by the other A+ Manual
modules. The module itself closes one day later so the early cutoff is within
the module's opening and closing times.

The early bonus settings apply to every assignment in this module. 
:early-time: sets the bonus cutoff, which must fall after the module opens 
and before it closes. A submission must be made before that timestamp to qualify; 
one submitted exactly at the cutoff does not.

:early-bonus: sets the extra-points fraction: for example, 0.1 adds 10% to 
points earned. The valueless :early-bonus-in-use: flag activates the configured 
bonus; without it, no bonus is applied.

Optionally, :bonus-time-step-hours: makes the bonus decrease in steps after 
the early cutoff. For example, with 24, the bonus decreases every 24 hours until 
the module closes; any final partial interval receives no bonus. Omitting this field 
(or setting it to 0) disables the stepwise decrease.

.. toctree::

  exercise

.. aplusmeta::
  :close-time: 2031-01-01 12:00
  :early-time: 2030-12-31 12:00
  :early-bonus: 0.1
  :early-bonus-in-use:
  :bonus-time-step-hours: 0
  