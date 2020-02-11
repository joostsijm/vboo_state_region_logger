"""Main app"""

import sys
import time

from app import SCHEDULER, LOGGER, jobs, job_storage


if __name__ == '__main__':
    # jobs
    # jobs.update_regions(2981)
    # sys.exit()

    # Jobs
    JOBS = job_storage.get_jobs()
    for state_id in JOBS:
        LOGGER.info('"%s" add update job', state_id,)
        SCHEDULER.add_job(
            jobs.update_regions,
            'cron',
            args=[state_id],
            id='{}_update_regions'.format(state_id),
            replace_existing=True,
            hour='12'
        )

    try:
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        print('Exiting application')
        SCHEDULER.shutdown()
        sys.exit()
