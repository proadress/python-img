'use client'
import { Button } from '@/components/ui/button';
import Link from 'next/link';
import React, { useState } from 'react';

export const Menu = () => {
    const [showXRayOptions, setShowXRayOptions] = useState(false);
    const [showLicensePlateOptions, setShowLicensePlateOptions] = useState(false);

    return (
        <div className='flex flex-row gap-4'>
            <div>
                <Button onClick={() => setShowXRayOptions(!showXRayOptions)}>x光 - {showXRayOptions ? '收合' : '展開'}</Button>
                {showXRayOptions && (
                    <div>
                        <Link href="/xray/single"><Button>單</Button></Link>
                        <Link href="/xray/multiple"><Button>-多</Button></Link>
                    </div>
                )}
            </div>
            <div>
                <Button onClick={() => setShowLicensePlateOptions(!showLicensePlateOptions)}>車牌 - {showLicensePlateOptions ? '收合' : '展開'}</Button>
                {showLicensePlateOptions && (
                    <div>
                        <Link href="/car/single"><Button>單</Button></Link>
                        <Button>-連續</Button>
                    </div>
                )}
            </div>
        </div>
    );
}