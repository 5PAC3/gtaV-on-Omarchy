#include <windows.h>
#include <string.h>
#include <errno.h>

static const char *get_error_msg(int errnum)
{
    switch (errnum) {
        case 0:      return "No error";
        case EINVAL:  return "Invalid argument";
        case ERANGE:  return "Result too large";
        case ENOMEM:  return "Not enough memory";
        case EFAULT:  return "Bad address";
        case EBADF:   return "Bad file descriptor";
        case ENOENT:  return "No such file or directory";
        case ENOSPC:  return "No space left on device";
        case EACCES:  return "Permission denied";
        case EEXIST:  return "File exists";
        case EISDIR:  return "Is a directory";
        case ENOTDIR: return "Not a directory";
        case ENFILE:  return "Too many open files";
        case EMFILE:  return "Too many open files";
        case EPERM:   return "Operation not permitted";
        case EBUSY:   return "Device or resource busy";
        case ETXTBSY: return "Text file busy";
        case ESPIPE:  return "Illegal seek";
        case EROFS:   return "Read-only file system";
        case ENOTEMPTY: return "Directory not empty";
        case ECONNRESET: return "Connection reset by peer";
        case ECONNREFUSED: return "Connection refused";
        case EHOSTUNREACH: return "No route to host";
        case ENETUNREACH: return "Network is unreachable";
        case ETIMEDOUT: return "Connection timed out";
        case ENETDOWN: return "Network is down";
        case EHOSTDOWN: return "Host is down";
        default: {
            static char unknown_buf[64];
            snprintf(unknown_buf, sizeof(unknown_buf), "Unknown error: %d", errnum);
            return unknown_buf;
        }
    }
}

errno_t __cdecl _strerror_s(char *buffer, size_t sizeInChars, int errnum)
{
    if (!buffer || sizeInChars == 0) {
        return EINVAL;
    }

    const char *msg = get_error_msg(errnum);
    size_t len = strlen(msg);

    if (len >= sizeInChars) {
        if (sizeInChars > 0) {
            buffer[0] = '\0';
        }
        return ERANGE;
    }

    strcpy(buffer, msg);
    return 0;
}
