# txtclock

Nice and simple text-based clock written in Python.

```
  11111      0000000           333333333        11111          0000000            6666666
1111111     0000000000         33333333333    1111111         0000000000        666666666
111 111    0000    0000        33      333    111 111        0000    0000      66666
    111   000        000  ##           3333       111   ##  000        000    666
    111   000        000  ##           333        111   ##  000        000   666
    111   000        000         33333333         111       000        000   66666666666
    111   000        000         3333333          111       000        000  66666666666666
    111   000        000            333333        111       000        000  6666       666
    111   000        000               3333       111       000        000  666        6666
    111   000        000                333       111       000        000  666        6666
    111   0000      0000  ##            333       111   ##  0000      0000   666       666
    111    0000    0000   ##   33      3333       111   ##   0000    0000    6666     6666
    111     0000000000        333333333333        111         0000000000      66666666666
    111       000000           333333333          111           000000          6666666

                                       2021/12/17

              ░░░░░░······················································
```

## Usage
```
$ txtclock
```

Use the following keys while running:
|key|function|
|---|---|
|`ESC` / `CTRL+C` / `Q`|exit|
|`B`|Show/hide the seconds bar|
|`C`|Cycle through colors|
|`D`|Show/hide the date|
|`F`|Cycle through fonts|
|`H`|Show/hide the help bar|

## Configuration
* Create a folder for `txtclock` configuration:
    ```
    $ mkdir -p ~/.config/txtclock
    ```
* Create a config file with defaults:
    ```
    $ txtclock --write_config ~/.config/txtclock
    ```
* Edit config file:
    ```
    $ bash -c "$EDITOR ~/.config/txtclock/txtclock.conf"
    ```

### Config values
```ini
[txtclock]
utc = False
font = numnum
show_date = True
show_seconds_bar = True
seconds_bar_size = 60
second_bar_fill_char = ░
second_bar_empty_char = ·
show_help = False
time_format = %%H:%%M:%%S
date_format = %%Y/%%m/%%d
numbers_color = green
```
|variable|description|
|---|---|
|`utc`|Use UTC time?|
|`font`|Clock font name|
|`show_date`|Show date?|
|`show_seconds_bar`|Show seconds bar?|
|`seconds_bar_size`|Seconds bar size (characters)|
|`second_bar_fill_char`|Fill char for the bar|
|`second_bar_empty_char`|Empty char for the bar|
|`show_help`|Show help bar?|
|`time_format`|Time format|
|`date_format`|Date format|
|`numbers_color`|Color for numbers|

## Parameters
All configuration variables are accesible as parameters:
```
$ txtclock -h
usage: txtclock [-h] [--write_config WRITE_CONFIG] [--config_file CONFIG_FILE] [--utc UTC] [-f FONT] [-d SHOW_DATE] [-b SHOW_SECONDS_BAR]
                [--seconds_bar_size SECONDS_BAR_SIZE] [--second_bar_fill_char SECOND_BAR_FILL_CHAR] [--second_bar_empty_char SECOND_BAR_EMPTY_CHAR] [--show_help SHOW_HELP]
                [--time_format TIME_FORMAT] [--date_format DATE_FORMAT] [--numbers_color NUMBERS_COLOR]

optional arguments:
  -h, --help            show this help message and exit
  --write_config WRITE_CONFIG
                        write config file an exit
  --config_file CONFIG_FILE
                        set config file to use
  --utc UTC             use UTC instead of local time?
  -f FONT, --font FONT  select clock font
  -d SHOW_DATE, --show_date SHOW_DATE
                        show date?
  -b SHOW_SECONDS_BAR, --show_seconds_bar SHOW_SECONDS_BAR
                        show seconds bar?
  --seconds_bar_size SECONDS_BAR_SIZE
                        seconds bar size
  --second_bar_fill_char SECOND_BAR_FILL_CHAR
                        fill char for seconds bar
  --second_bar_empty_char SECOND_BAR_EMPTY_CHAR
                        fill char for seconds bar
  --show_help SHOW_HELP
                        show help bar?
  --time_format TIME_FORMAT
                        time format
  --date_format DATE_FORMAT
                        date format
  --numbers_color NUMBERS_COLOR
                        color for numbers
```


## Fonts

### default
```
                           10:29:44

                          2021/12/17

 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░················
```

### numnum


```
  11111          0000000             333333333          11111                0000000            6666666
1111111         0000000000           33333333333      1111111               0000000000        666666666
111 111        0000    0000          33      333      111 111              0000    0000      66666
    111       000        000    ##           3333         111         ##  000        000    666
    111       000        000    ##           333          111         ##  000        000   666
    111       000        000           33333333           111             000        000   66666666666
    111       000        000           3333333            111             000        000  66666666666666
    111       000        000              333333          111             000        000  6666       666
    111       000        000                 3333         111             000        000  666        6666
    111       000        000                  333         111             000        000  666        6666
    111       0000      0000    ##            333         111         ##  0000      0000   666       666
    111        0000    0000     ##   33      3333         111         ##   0000    0000    6666     6666
    111         0000000000          333333333333          111               0000000000      66666666666
    111           000000             333333333            111                 000000          6666666

                                                2021/12/17

                       ░░░░░░······················································
```




