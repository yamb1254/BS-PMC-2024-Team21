import { Helmet } from 'react-helmet-async';

import { LecturerView } from 'sections/student-sections/lecturer/view';

// ----------------------------------------------------------------------

export default function LeturerPage() {
  return (
    <>
      <Helmet>
        <title> Lecturers | LEARNIX </title>
      </Helmet>
      <LecturerView />
    </>
  );
}