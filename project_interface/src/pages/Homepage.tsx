import React, { useState } from 'react';
import logo from './logo.svg';
import '../styles/Homepage.css';
import Topbar from '../components/Topbar';
import TextField from '@mui/material/TextField';
import { Accordion, AccordionActions, AccordionDetails, AccordionSummary, Button, FilledInput, FormControl, FormHelperText, IconButton, InputAdornment, InputLabel, OutlinedInput } from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';


function Homepage() {
    const [age, setAge] = useState<string>('');
    const [ageError, setAgeError] = useState<string>('');

    const [sipa, setSipa] = useState<string>('');
    const [sipaError, setSipaError] = useState<string>('');

    const [hemoglobin, setHemoglobin] = useState<string>('');
    const [hemoglobinError, setHemoglobinError] = useState<string>('');

    const [bloodGiven, setBloodGiven] = useState<string>('');
    const [bloodGivenError, setBloodGivenError] = useState<string>('');

    const [showShock, setShowShock] = useState<boolean>(false);

  
    const handleAgeChange = (event: any) => {
      const inputAge = event.target.value;
      if (isNaN(Number(inputAge)) || Number(inputAge) < 4 || Number(inputAge) > 16) {
        setAgeError('Please enter a valid number between 4 and 16.');
      } else {
        setAgeError('');
      }
      calculateTotal();
      setAge(inputAge);
    };

    const handleSipaChange = (event: any) => {
        const inputSipa = event.target.value;
        if (isNaN(Number(inputSipa)) || Number(inputSipa) < 4 || Number(inputSipa) > 16) {
          setSipaError('Please enter a valid number.');
        } else {
            setSipaError('');
        }
        calculateTotal();
        setSipa(inputSipa);
    };

    const handleHemoglobinChange = (event: any) => {
        const inputHemoglobin = event.target.value;
        if (isNaN(Number(inputHemoglobin)) || Number(inputHemoglobin) < 4 || Number(inputHemoglobin) > 16) {
          setHemoglobinError('Please enter a valid number.');
        } else {
            setHemoglobinError('');
        }
        calculateTotal();
        setHemoglobin(inputHemoglobin);
    };

    const handleBloodGivenChange = (event: any) => {
        const inputBloodGiven = event.target.value;
        if (isNaN(Number(inputBloodGiven)) || Number(inputBloodGiven) < 4 || Number(inputBloodGiven) > 16) {
          setBloodGivenError('Please enter a valid number.');
        } else {
            setBloodGivenError('');
        }
        calculateTotal();
        setBloodGiven(inputBloodGiven);
    };

     // Calculate total and show shock if total is over the threshold (placeholder for now)
     const calculateTotal = () => {
        const total = Number(age) + Number(sipa) + Number(hemoglobin) + Number(bloodGiven);
        setShowShock(total > 10);
    };
  
  return (
      <div className='h-full w-full flex flex-col items-center justify-between'>
        <Topbar />
        {/* Input and Links container */}
        <div className='h-full w-full flex flex-row items-center justify-evenly p-5'>
            {/* Input container */}

            <div className='w-[60%] h-full flex flex-col items-center gap-2'>
                <div className='text-5xl font-bold drop-shadow-2xl mb-5 '>Shock Index </div>

                <FormControl sx={{ m: 1, width: 'full' }} variant="filled" fullWidth error={!!ageError}>
                    <InputLabel htmlFor="filled-adornment-password">Age</InputLabel>
                    <FilledInput
                       id="filled-adornment-weight"
                       fullWidth
                       value={age}
                       onChange={handleAgeChange}
                       endAdornment={<InputAdornment position="end">Years</InputAdornment>}
                       aria-describedby="age-error-text"
                       autoComplete='off'
                       inputProps={{
                         'aria-label': 'age',
                       }}
                    />
                    <FormHelperText id="age-error-text">{ageError}</FormHelperText>
                </FormControl>

                <FormControl sx={{ m: 1, width: 'full' }} variant="filled" fullWidth error={!!sipaError}>
                    <InputLabel htmlFor="filled-adornment-password">SIPA</InputLabel>
                    <FilledInput
                       id="filled-adornment-weight"
                       fullWidth
                       value={sipa}
                       onChange={handleSipaChange}
                       autoComplete='off'
                    //    endAdornment={<InputAdornment position="end">Years</InputAdornment>}
                       aria-describedby="age-error-text"
                    />
                    <FormHelperText id="age-error-text">{sipaError}</FormHelperText>
                </FormControl>

                <FormControl sx={{ m: 1, width: 'full' }} variant="filled" fullWidth error={!!hemoglobinError}>
                    <InputLabel htmlFor="filled-adornment-password">Hemoglobin</InputLabel>
                    <FilledInput
                       id="filled-adornment-weight"
                       fullWidth
                       value={hemoglobin}
                       onChange={handleHemoglobinChange}
                    //    endAdornment={<InputAdornment position="end">Years</InputAdornment>}
                       aria-describedby="age-error-text"
                       autoComplete='off'
                       inputProps={{
                         'aria-label': 'age',
                       }}
                    />
                    <FormHelperText id="age-error-text">{hemoglobinError}</FormHelperText>
                </FormControl>

                <FormControl sx={{ m: 1, width: 'full' }} variant="filled" fullWidth error={!!bloodGivenError}>
                    <InputLabel htmlFor="filled-adornment-password">Blood Given</InputLabel>
                    <FilledInput
                       id="filled-adornment-weight"
                       fullWidth
                       value={bloodGiven}
                       onChange={handleBloodGivenChange}
                    //    endAdornment={<InputAdornment position="end">Years</InputAdornment>}
                       aria-describedby="age-error-text"
                       autoComplete='off'
                       inputProps={{
                         'aria-label': 'age',
                       }}
                    />
                    <FormHelperText id="age-error-text">{bloodGivenError}</FormHelperText>
                </FormControl>

                <div className={`${showShock ? 'bg-red-500' : 'bg-blue-200'} w-full h-[40%] border ${showShock ? 'border-red-900' : 'border-blue-900'} rounded-lg shadow-lg flex p-5`}>
                    <div className={`font-bold text-3xl text-white`}>{showShock ? 'CHILD IN SHOCK' : 'Results'}</div>
                </div>
            </div>

            {/* Link Container */}
            <div className=' flex flex-col w-[30%] h-full gap-5 '>
                {/* <div className='flex flex-row justify-center bg-blue-200 h-[30%]  rounded-lg p-3 border border-blue-900 shadow-lg'>
                    <div className='font-semibold text-2xl text-blue-900'>Info</div>
                </div> */}

                <div className='flex flex-col shadow-md'>
                    <div className='text-2xl font-bold'>Info</div>
                    <Accordion>
                        <AccordionSummary
                        expandIcon={<ExpandMoreIcon />}
                        aria-controls="panel1-content"
                        id="panel1-header"
                        >
                        Details
                        </AccordionSummary>
                        <AccordionDetails>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                        malesuada lacus ex, sit amet blandit leo lobortis eget.
                        </AccordionDetails>
                    </Accordion>
                    <Accordion>
                        <AccordionSummary
                        expandIcon={<ExpandMoreIcon />}
                        aria-controls="panel2-content"
                        id="panel2-header"
                        >
                        Algorithm
                        </AccordionSummary>
                        <AccordionDetails>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                        malesuada lacus ex, sit amet blandit leo lobortis eget.
                        </AccordionDetails>
                    </Accordion>
                    <Accordion>
                        <AccordionSummary
                        expandIcon={<ExpandMoreIcon />}
                        aria-controls="panel3-content"
                        id="panel3-header"
                        >
                        Neural Network
                        </AccordionSummary>
                        <AccordionDetails>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                        malesuada lacus ex, sit amet blandit leo lobortis eget.
                        </AccordionDetails>
                        <AccordionActions>
                            <Button>Cancel</Button>
                            <Button>Agree</Button>
                        </AccordionActions>
                    </Accordion>
                </div>
                <div className='flex flex-row justify-center h-full rounded-lg p-3 border border-gray-500 shadow-lg'>
                    <div className='font-semibold text-2xl text-gray-900'>Relevant Links</div>
                </div>
            </div>
        </div>
    </div>
  );
}

export default Homepage;
