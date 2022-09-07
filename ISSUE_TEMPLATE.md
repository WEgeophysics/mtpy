<!--- Provide a general summary of your changes in the Title above -->

<!--- To help us understand and resolve your issue, please fill out the form to the best of your ability.-->
<!--- You can feel free to delete the sections that do not apply.-->

Skip the second and minutes assertion errors 

I have got a 238 EDI-files last month  ago and some second and minutes end up to 60. An error raises everytimes the value equals to 60. 
To skip this asserion error, I suggest to restart counting. For instance 12:25min:60s ==> 12:26min:00s since it is difficult for users to everytimes convert 
value manually himself. 


## Expected Behavior
<!--- If you're describing a bug, tell us what should happen -->
<!--- If you're suggesting a change/improvement, tell us how it should work -->
Skip assertion error and do it automatically 

## Current Behavior
<!--- If describing a bug, tell us what happens instead of the expected behavior -->
<!--- If suggesting a change/improvement, explain the difference from current behavior -->

## Possible Solution
<!--- Not obligatory, but suggest a fix/reason for the bug, -->
<!--- or ideas how to implement the addition or change -->
restart the counting to avoid multiples Assertion Error especially when we have many sites to process.

## Steps to Reproduce (for bugs)
<!--- Provide a link to a live example, or an unambiguous set of steps to -->
<!--- reproduce this bug. Include code to reproduce, if relevant -->
1. write a helpers functions `_restart_count`
2. insert function in function `convert_position_str2float` 
3.
4.

<!--- A minimum code snippet required to reproduce the bug, also minimizing the number of dependencies required-->

```python
# Paste your code here

def _restart_count(deg_or_min, value):
    """ restart the countdown and skip error if seconds or minutes are equal to 60. 
    
    Commonly seconds and minutes should not end by 60. However, some EDI-files rewritten by some hardwares
    end up minutes and second with 60. To avoid the  AssertionError at everytimes the mtobj is created,
    the second and minutes should restart automatically.   
    """
    return ( deg_or_min + value//60, value%60 )  if float (value) >=60. else (
        deg_or_min, value )  

def convert_position_str2float(position_str):
    """
    Convert a position string in the format of DD:MM:SS to decimal degrees

    :type position_str: string [ 'DD:MM:SS.ms' | 'DD.degrees' ]
    :param position_str: degrees of latitude or longitude

    :rtype: float
    :return: latitude or longitude in decimal degrees

    :Example: ::

        >>> from mtpy.utils import gis_tools
        >>> gis_tools.convert_position_str2float('-118:34:56.3')
        -118.58230555555555

    """

    if position_str in [None, 'None']:
        return None

    if ':' in position_str:
        if position_str.count(':') != 2:
            msg = '{0} not correct format.\n'.format(position_str) +\
                  'Position needs to be DD:MM:SS.ms'
            raise GISError(msg)
        p_list = position_str.split(':')
        #----------------------------------------------
        deg = float(p_list[0])
        minutes = float(p_list[1])
        sec = float(p_list[2])
        minutes, sec = _restart_count(minutes, sec) 
        deg, minutes =  _restart_count(deg, minutes) 
        #--------------------------------------------------
        sign = np.sign(deg)

        position_value = sign * (abs(deg) + minutes / 60. + sec / 3600.)
    else:
        try:
            position_value = float(position_str)
        except ValueError:
            msg = '{0} not correct format.\n'.format(position_str) +\
                  'Position needs to be DD.decimal_degrees'
            raise GISError(msg)

    return position_value
```

## Context
<!--- How has this issue affected you? What are you trying to accomplish? -->
<!--- Providing context helps us come up with a solution that is most useful in the real world -->
Not easy to nanually modify everytimes the DD:MM:SS in 528 sites everytimes values equals to 60. 

## Your Environment
<!--- Include as many relevant details about the environment you experienced the bug in -->
  * Operating system:Window10
  * MtPy version: 1.5
  * Python version:3.9
<!---if it is data visualization related, also provide-->
  * Matplotlib version:
  * Matplotlib backend (`print(matplotlib.get_backend())`):
<!---if it is graphical user interface (GUI) related-->
  * QT version:

**Installed Python Packages:**
use `pip freeze` or `conda list [-n ENVIRONMENT_NAME]` to list all the installed libraries.

