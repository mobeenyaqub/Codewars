#include <stdbool.h>

const char *boolean_to_string(bool b)
{
    if (b)
        return "true";
    return "false";
}