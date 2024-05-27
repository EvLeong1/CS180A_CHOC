import React, { useState } from 'react';
import logo from './logo.svg';
import '../styles/Homepage.css';
import Topbar from '../components/Topbar';
// import TextField from '@mui/material/TextField';
import { Accordion, AccordionActions, AccordionDetails, AccordionSummary, Button, FilledInput, FormControl, FormHelperText, IconButton, InputAdornment, InputLabel, OutlinedInput } from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import axios from 'axios';
import Link from '@mui/material/Link';

type Prediction = {
    prediction_class0: number;
    prediction_class1: number;
}

function Homepage() {
    const [age, setAge] = useState<string>('');
    const [ageError, setAgeError] = useState<string>('');

    const [los_floor, setLos_floor] = useState<string>('');

    const [mtp, setMtp] = useState<string>('');

    const [initial_hb, setInitial_hb] = useState<string>('');
    const [hours_admit, setHours_admit] = useState<string>('');
    const [current_hb, setCurrent_hb] = useState<string>('');

    const [sbp_low, setSbp_low] = useState<string>('');
    const [sbp_high, setSbp_high] = useState<string>('');

    const [dbp_low, setDbp_low] = useState<string>('');
    const [dbp_high, setDbp_high] = useState<string>('');



    const [showShock, setShowShock] = useState<boolean>(false);
    const [prediction, setPrediction] = useState<Prediction>({prediction_class0: 0, prediction_class1: 0});
    

    //  // Calculate total and show shock if total is over the threshold (placeholder for now)
    //  const calculateTotal = () => {
    //     const total = Number(age) + Number(sipa) + Number(hemoglobin) + Number(bloodGiven);
    //     setShowShock(total > 10);
    // };

    

    const handleSubmit = async () => {
        try {
            console.log('Submitting:', los_floor, mtp, initial_hb, hours_admit, current_hb, sbp_low, sbp_high, dbp_low, dbp_high);
            const response = await axios.post('http://localhost:5000/predict', {
                los_floor: los_floor,
                mtp: mtp,
                initial_hb: initial_hb,
                hours_admit: hours_admit,
                current_hb: current_hb,
                sbp_low: sbp_low,
                sbp_high: sbp_high,
                dbp_low: dbp_low,
                dbp_high: dbp_high
            });

            setPrediction(response.data);
            console.log('Prediction:', response.data);
        } catch (error) {
            console.error('Error predicting:', error);
        }
    };


  
  return (
    <div className='h-full w-full flex flex-col items-center justify-between'>
        <Topbar />
        <div className='h-full w-full flex flex-row items-center justify-evenly p-5'>
            <div className='w-[60%] h-full flex flex-col items-center gap-2'>
                <div className='text-5xl font-bold drop-shadow-2xl mb-5 '>Pediatric Intervention</div>
                <div className='flex flex-row w-[100%] gap-5'>
                    <FormControl variant="filled" fullWidth error={!!ageError}>
                        <InputLabel htmlFor="filled-adornment-los-floor">Length of Stay on Floor</InputLabel>
                        <FilledInput
                            id="filled-adornment-los-floor"
                            fullWidth
                            value={los_floor}
                            onChange={(e) => setLos_floor(e.target.value)}
                            endAdornment={<InputAdornment position="end">Hours</InputAdornment>}
                            aria-describedby="los-floor-error-text"
                            autoComplete='off'
                            inputProps={{ 'aria-label': 'los_floor' }}
                        />
                        <FormHelperText id="los-floor-error-text">{ageError}</FormHelperText>
                    </FormControl>
                    <FormControl variant="filled" fullWidth error={!!ageError}>
                        <InputLabel htmlFor="filled-adornment-mtp">Massive Transusion Protocol initiated?</InputLabel>
                        <FilledInput
                            id="filled-adornment-mtp"
                            fullWidth
                            value={mtp}
                            onChange={(e) => setMtp(e.target.value)}
                            endAdornment={<InputAdornment position="end"></InputAdornment>}
                            aria-describedby="mtp-error-text"
                            autoComplete='off'
                            inputProps={{ 'aria-label': 'mtp' }}
                        />
                        <FormHelperText id="mtp-error-text">{ageError}</FormHelperText>
                    </FormControl>
                </div>

                <div className='flex flex-col w-[100%] '>
                    <p className='font-bold text-lg text-blue-900'>Hemoglobin</p>
                    <div className='flex flex-row w-[100%] gap-5 mt-1'>
                        <FormControl variant="filled" fullWidth error={!!ageError}>
                            <InputLabel htmlFor="filled-adornment-initial-hb">Initial HB</InputLabel>
                            <FilledInput
                                id="filled-adornment-initial-hb"
                                fullWidth
                                value={initial_hb}
                                onChange={(e) => setInitial_hb(e.target.value)}
                                aria-describedby="initial-hb-error-text"
                                autoComplete='off'
                                inputProps={{ 'aria-label': 'initial_hb' }}
                            />
                            <FormHelperText id="initial-hb-error-text">{ageError}</FormHelperText>
                        </FormControl>
                        <FormControl variant="filled" fullWidth error={!!ageError}>
                            <InputLabel htmlFor="filled-adornment-hours-admit">Hours since admit</InputLabel>
                            <FilledInput
                                id="filled-adornment-hours-admit"
                                fullWidth
                                value={hours_admit}
                                onChange={(e) => setHours_admit(e.target.value)}
                                endAdornment={<InputAdornment position="end"></InputAdornment>}
                                aria-describedby="hours-admit-error-text"
                                autoComplete='off'
                                inputProps={{ 'aria-label': 'hours_admit' }}
                            />
                            <FormHelperText id="hours-admit-error-text">{ageError}</FormHelperText>
                        </FormControl>
                        <FormControl variant="filled" fullWidth error={!!ageError}>
                            <InputLabel htmlFor="filled-adornment-current-hb">Current HB</InputLabel>
                            <FilledInput
                                id="filled-adornment-current-hb"
                                fullWidth
                                value={current_hb}
                                onChange={(e) => setCurrent_hb(e.target.value)}
                                endAdornment={<InputAdornment position="end"></InputAdornment>}
                                aria-describedby="current-hb-error-text"
                                autoComplete='off'
                                inputProps={{ 'aria-label': 'current_hb' }}
                            />
                            <FormHelperText id="current-hb-error-text">{ageError}</FormHelperText>
                        </FormControl>
                    </div>
                </div>

                <div className='flex flex-col w-[100%] '>
                    <p className='font-bold text-lg text-blue-900'>SBP</p>
                    <div className='flex flex-row w-[100%] gap-5 mt-1'>
                        <FormControl variant="filled" fullWidth error={!!ageError}>
                            <InputLabel htmlFor="filled-adornment-sbp-low">Low</InputLabel>
                            <FilledInput
                                id="filled-adornment-sbp-low"
                                fullWidth
                                value={sbp_low}
                                onChange={(e) => setSbp_low(e.target.value)}
                                aria-describedby="sbp-low-error-text"
                                autoComplete='off'
                                inputProps={{ 'aria-label': 'sbp_low' }}
                            />
                            <FormHelperText id="sbp-low-error-text">{ageError}</FormHelperText>
                        </FormControl>
                        <FormControl variant="filled" fullWidth error={!!ageError}>
                            <InputLabel htmlFor="filled-adornment-sbp-high">High</InputLabel>
                            <FilledInput
                                id="filled-adornment-sbp-high"
                                fullWidth
                                value={sbp_high}
                                onChange={(e) => setSbp_high(e.target.value)}
                                endAdornment={<InputAdornment position="end"></InputAdornment>}
                                aria-describedby="sbp-high-error-text"
                                autoComplete='off'
                                inputProps={{ 'aria-label': 'sbp_high' }}
                            />
                            <FormHelperText id="sbp-high-error-text">{ageError}</FormHelperText>
                        </FormControl>
                    </div>
                </div>

                <div className='flex flex-col w-[100%] '>
                    <p className='font-bold text-lg text-blue-900'>DBP</p>
                    <div className='flex flex-row w-[100%] gap-5 mt-1'>
                        <FormControl variant="filled" fullWidth error={!!ageError}>
                            <InputLabel htmlFor="filled-adornment-dbp-low">Low</InputLabel>
                            <FilledInput
                                id="filled-adornment-dbp-low"
                                fullWidth
                                value={dbp_low}
                                onChange={(e) => setDbp_low(e.target.value)}
                                aria-describedby="dbp-low-error-text"
                                autoComplete='off'
                                inputProps={{ 'aria-label': 'dbp_low' }}
                            />
                            <FormHelperText id="dbp-low-error-text">{ageError}</FormHelperText>
                        </FormControl>
                        <FormControl variant="filled" fullWidth error={!!ageError}>
                            <InputLabel htmlFor="filled-adornment-dbp-high">High</InputLabel>
                            <FilledInput
                                id="filled-adornment-dbp-high"
                                fullWidth
                                value={dbp_high}
                                onChange={(e) => setDbp_high(e.target.value)}
                                endAdornment={<InputAdornment position="end"></InputAdornment>}
                                aria-describedby="dbp-high-error-text"
                                autoComplete='off'
                                inputProps={{ 'aria-label': 'dbp_high' }}
                            />
                            <FormHelperText id="dbp-high-error-text">{ageError}</FormHelperText>
                        </FormControl>
                    </div>
                </div>

                <Button
                    variant="contained"
                    color="primary"
                    onClick={handleSubmit}
                    className='w-full mt-4'
                >
                    Submit
                </Button>

                {prediction && (
                    <div className='w-full mt-4'>
                        <p className='text-xl font-bold'>Prediction Class 0: {prediction.prediction_class0 ?? 'N/A' }</p>
                        <p className='text-xl font-bold'>Prediction Class 1: {prediction.prediction_class1 ?? 'N/A' }</p>
                    </div>
                )}
            </div>
             {/* Link Container */}
        <div className=' flex flex-col w-[30%] h-full gap-5 '>


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
                Our task is to convert a well-known, static decision algorithm into a dynamic machine learning model 
                which classifies whether a child experiencing blunt trauma in their solid organs requires surgery, 
                mimicking clinical emergency decision making in real time to boost physician confidence.
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
                Our algorithm mimics the ATOMAC guidelines that clinicians use in order to determine the need for
                operative intervention in cases of liver and spleen blunt force trauma. For more information follow <br></br> 
                 <Link href="https://www.sciencedirect.com/science/article/pii/S0022346818306584">this link</Link>.
                </AccordionDetails>
            </Accordion>
            <Accordion>
                <AccordionSummary
                expandIcon={<ExpandMoreIcon />}
                aria-controls="panel3-content"
                id="panel3-header"
                >
                Variable Selection
                </AccordionSummary>
                <AccordionDetails>
                Through training of random forests and bagging, information gain was calculated to determine
                which features had the most impact in determining clinical intervention. The variables to the left 
                were deemed to be the most important, which include Length of Stay, MTP, Hemoglobin Levels, Systolic 
                Blood Pressure, and Diastolic Blood Pressure.
                </AccordionDetails>
            </Accordion>
        </div>
        <div className='flex flex-row justify-center h-full rounded-lg p-3 border border-gray-500 shadow-lg'>
            <div className='font-semibold text-2xl text-gray-900 flex flex-col  items-center gap-5'>
                <p>Relevant Links</p>
                <ul className='flex flex-col gap-2'>
                    <li className='text-sm flex flex-row items-center justify-between gap-5'>
                        <p>Project GitHub</p>
                        <a href="https://github.com/EvLeong1/CS180A_CHOC" className='text-blue-300'>https://github.com/EvLeong1/CS180A_CHOC</a>
                    </li>
                    <li className='text-sm flex flex-row items-center justify-between gap-5'>
                        <p>LNN Research</p>
                        <a href="https://arxiv.org/abs/2003.04630" className='text-blue-300'>https://arxiv.org/abs/2003.04630</a>
                    </li>
                </ul>
            </div>
        </div>
        </div>
        </div>
    
       
        </div>
    
  );
}

export default Homepage;
